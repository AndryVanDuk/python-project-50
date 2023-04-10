from gendiff.gendiff_base import generate_diff


__all__ = (
    'generate_diff',
)

print(generate_diff('file1.json', 'file2.json'))