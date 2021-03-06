import pytest
from genome_windows_generator import GenomeWindowsGenerator


def test_wrong_parameter():

    # Test invalid n_type
    with pytest.raises(ValueError):
        GenomeWindowsGenerator(
            assembly="hg19",
            window_size=200,
            batch_size=3,
            buffer_size=5,
            train_chromosomes=["chr1"],
            val_chromosomes=["chr2"],
            clear_cache=True,
            cache_dir="/tmp",
            n_type="INVALID_TYPE"
        )

    # Test too big windows
    with pytest.raises(ValueError):
        GenomeWindowsGenerator(
            assembly="hg19",
            window_size=200,
            batch_size=3,
            buffer_size=5,
            train_chromosomes=["chr1"],
            val_chromosomes=[],
            clear_cache=True,
            cache_dir="/tmp",
        ).validation_data()
