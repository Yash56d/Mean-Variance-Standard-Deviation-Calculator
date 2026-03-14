import numpy as np

def calculate(list_values):
    # Check if list has exactly 9 numbers
    if len(list_values) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 NumPy array
    matrix = np.array(list_values).reshape(3, 3)

    # Build dictionary with required statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations

# Example usage
if __name__ == "__main__":
    input_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(input_values)
    print(result)