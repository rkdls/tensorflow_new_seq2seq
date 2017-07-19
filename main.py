import tensorflow as tf
from tensorflow.python.layers import core as layers_core


class BaseModel(object):
    def __init__(self, X, Y, sequence_length, vocab, scope=None):
        vocab_size = len(vocab)
        embedding_size = 50
        self.num_units = 50
        self.sequence_length = sequence_length

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
            logits, sample_id, final_context_state = self._build_decoder(encoder_outputs, encoder_state, hparams)

    def _build_encoder(self, params):
        with tf.variable_scope("encoder") as scope:
            encoder_emb_inp = tf.nn.embedding_lookup(self.embedding, params[0])
            grucell = tf.contrib.rnn.GRUCell(self.num_units)
            encoder_outputs, encoder_state = tf.nn.dynamic_rnn(grucell, encoder_emb_inp, dtype=tf.float32,
                                                               sequence_length=self.sequence_length)

        return encoder_outputs, encoder_state

    def _build_decoder(self):
        tgt_sos_id = tf.cast(self.tgt_vocab_table.lookup(tf.constant(hparams.sos)),
                             tf.int32)
        tgt_eos_id = tf.cast(self.tgt_vocab_table.lookup(tf.constant(hparams.eos)),
                             tf.int32)
