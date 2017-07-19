import tensorflow as tf
from tensorflow.python.layers import core as layers_core
from tensorflow.python.ops import lookup_ops

UNK_WORD = '§<OOV>§'
START_WORD = '§<START>§'
END_WORD = '§<END>§'

vocab_file = 'vocab.csv'
vocab_table = lookup_ops.index_table_from_file(vocab_file, default_value=UNK_WORD)


def create_attention_mechanism(num_units, memory, sequence_length):
    attention_mechanism = tf.contrib.seq2seq.BahdanauAttention(
        num_units, memory, memory_sequence_length=sequence_length)

    return attention_mechanism


class BaseModel(object):
    def __init__(self, X, Y, sequence_length, vocab, batch_size, scope=None):
        vocab_size = len(vocab)
        embedding_size = 50
        self.num_units = 50
        self.sequence_length = sequence_length
        self.beam_width = 5
        self.batch_size = batch_size

        with tf.variable_scope(scope or 'build_network'):
            with tf.variable_scope("decoder/output_projection"):
                self.output_layer = layers_core.Dense(
                    vocab_size, use_bias=False, name="output_projection")

        self.embedding = tf.get_variable(
            "embedding_share", [vocab_size, embedding_size], tf.float32)

        params = (X, Y)
        res = self.build_graph(params, scope=scope)

    def build_graph(self, params, scope):
        with tf.variable_scope(scope or "dynamic_seq2seq", dtype=tf.float32):
            encoder_outputs, encoder_state = self._build_encoder(params)
            logits, sample_id, final_context_state = self._build_decoder(encoder_outputs, encoder_state, params)

            if self.mode != tf.contrib.learn.ModeKeys.INFER:
                loss = self._compute_loss(logits, params)

    def _compute_loss(self, logits, params):
        target_output = params[1]
        target_output = tf.transpose(target_output)

        max_time = self.get_max_time(target_output)

        crossent = tf.nn.sparse_softmax_cross_entropy_with_logits(
            labels=target_output, logits=logits)

        target_weights = tf.sequence_mask(self.sequence_length, max_time, dtype=logits.dtype)


    def get_max_time(self, tensor):
        time_axis = 1
        return tensor.shape[time_axis].value or tf.shape(tensor)[time_axis]

    def _build_encoder(self, params):
        with tf.variable_scope("encoder") as scope:
            encoder_emb_inp = tf.nn.embedding_lookup(self.embedding, params[0])
            grucell = tf.contrib.rnn.GRUCell(self.num_units)
            encoder_outputs, encoder_state = tf.nn.dynamic_rnn(grucell, encoder_emb_inp, dtype=tf.float32,
                                                               sequence_length=self.sequence_length)

        return encoder_outputs, encoder_state

    def _build_decoder(self, encoder_outputs, encoder_state, params):
        tgt_sos_id = tf.cast(vocab_table.lookup(tf.constant(START_WORD)), tf.int32)
        tgt_eos_id = tf.cast(vocab_table.lookup(tf.constant(END_WORD)), tf.int32)

        decoding_length_factor = 2.0
        max_encoder_length = tf.reduce_max(self.sequence_length)
        maximum_iterations = tf.to_int32(tf.round(tf.to_float(max_encoder_length) * decoding_length_factor))

        with tf.variable_scope("decoder") as decoder_scope:
            cell, decoder_initial_state = self._build_decoder_cell(encoder_outputs, encoder_state)
            if self.mode != tf.contrib.learn.ModeKeys.INFER:
                # target_input = (batch_size, max_time)
                target_input = params[1]
                target_input = tf.transpose(target_input)

                # decoder_emp_inp: [max_time, batch_size, num_units]
                decoder_emb_inp = tf.nn.embedding_lookup(self.embedding, target_input)
                helper = tf.contrib.seq2seq.TrainingHelper(decoder_emb_inp, self.sequence_length,
                                                           time_major=True)
                my_decoder = tf.contrib.seq2seq.BasicDecoder(cell, helper, decoder_initial_state)
                outputs, final_context_state, _ = tf.contrib.seq2seq.dynamic_decode(
                    my_decoder,
                    output_time_major=True,
                    swap_memory=True,
                    scope=decoder_scope)

                sample_id = outputs.sample_id
                logits = self.output_layer(outputs.rnn_output)

        return logits, sample_id, final_context_state

    def _build_decoder_cell(self, encoder_outputs, encoder_state):

        num_units = self.num_units
        beam_width = self.beam_width

        memory = encoder_outputs
        memory = tf.contrib.seq2seq.tile_batch(memory, multiplier=beam_width)

        if self.mode == 'inference' and beam_width > 0:
            memory = tf.contrib.seq2seq.tile_batch(
                memory, multiplier=beam_width)
            source_sequence_length = tf.contrib.seq2seq.tile_batch(
                self.sequence_length, multiplier=beam_width)
            encoder_state = tf.contrib.seq2seq.tile_batch(
                encoder_state, multiplier=beam_width)
            batch_size = self.batch_size * beam_width
        else:
            batch_size = self.batch_size

        attention_mechanism = create_attention_mechanism(num_units, memory, self.sequence_length)

        grucell = tf.contrib.rnn.GRUCell(self.num_units)

        alignment_history = (self.mode == 'inference' and beam_width == 0)

        cell = tf.contrib.seq2seq.AttentionWrapper(
            grucell,
            attention_mechanism,
            attention_layer_size=num_units,
            alignment_history=alignment_history,
            name="attention")

        decoder_initial_state = cell.zero_state(batch_size, tf.flaot32)

        return cell, decoder_initial_state


if __name__ == '__main__':
    tf.contrib.learn.ModeKeys.validate()
    BaseModel()
