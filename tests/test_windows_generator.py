from windows_generator import WindowsGenerator
data_generator = WindowsGenerator(
    assembly="hg19",
    window_size=200,
    batch_size=3,
    buffer_size=5,
    test_chromosomes=["chr1", "chr5"]
)

x, y = next(data_generator.train())