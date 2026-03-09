import numpy as np
import matplotlib.pyplot as plt


class SubspaceVisualizer:
    def __init__(self):
        # Setting up a 3D plotting environment
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

    def plot_subspace_plane(self, v1, v2):
        """
        Takes two vectors and 'spans' them to show the subspace (plane).
        """
        # 1. Create a grid of scalars (linear combinations)
        scalars = np.linspace(-2, 2, 10)
        S1, S2 = np.meshgrid(scalars, scalars)

        # 2. Compute the plane: Span = a*v1 + b*v2
        X = S1 * v1[0] + S2 * v2[0]
        Y = S1 * v1[1] + S2 * v2[1]
        Z = S1 * v1[2] + S2 * v2[2]

        # 3. Draw the surface
        self.ax.plot_surface(X, Y, Z, alpha=0.3, color='blue')

        # 4. Draw the original 'Basis' vectors as arrows
        self.ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='red', label='Basis V1')
        self.ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='green', label='Basis V2')

        self.v1 = v1
        self.v2 = v2

    def add_test_vector(self, v3):
        """
        Plots a third vector and calculates if it 'breaks' the 2D subspace.
        """
        # 1. Plot the test vector in a different color (Gold)
        self.ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='gold', label='Test Vector', linewidth=4)

        # 2. Check for Linear Independence using Matrix Rank
        # We stack the vectors into a matrix and check its dimension
        matrix = np.array([vec_a, vec_b, v3])
        rank = np.linalg.matrix_rank(matrix)

        if rank < 3:
            print(f"\nSTATUS: DEPENDENT. Vector {v3} lives INSIDE the plane.")
        else:
            print(f"\nSTATUS: INDEPENDENT. Vector {v3} breaks OUT of the plane.")

    def finalize(self):
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.legend()
        plt.show()


# --- Running the Experiment ---
if __name__ == "__main__":
    viz = SubspaceVisualizer()

    vec_a = np.array([1, 2, 0])
    vec_b = np.array([0, 2, 1])
    viz.plot_subspace_plane(vec_a, vec_b)

    # SCENARIO 1: Redundant Vector (A combination of A and B)
    # This vector stays on the purple/blue plane.
    v_redundant = vec_a + vec_b
    viz.add_test_vector(v_redundant)

    # SCENARIO 2: Independent Vector (Adds a new dimension)
    # This vector will point straight "up" away from the plane.
    # v_independent = np.array([0, 0, 5])
    # viz.add_test_vector(v_independent)

    viz.finalize()