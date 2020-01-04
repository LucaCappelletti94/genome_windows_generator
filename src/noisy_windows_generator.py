

class NoisyWindowsGenerator(WindowsGenerator):

    def _buffer_encoder_generator(self, dataset):
        for buff_n, buffer in enumerate(self._buffer_generator(dataset)):
            yield list(self.pool.imap(
                one_hot_noise,
                (
                     (buff_n * self.buffer_size + i, sequences, self.n_type, self._mean, self._cov)
                    for i, sequences in enumerate(buffer)
                )
            ))