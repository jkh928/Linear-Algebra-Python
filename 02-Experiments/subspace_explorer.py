# ======================================================================
# SECTION: SUBSPACE VISUALIZER (SPAN & LINEAR INDEPENDENCE)
# COMPLEXITY: O(k^2) - Where 'k' is the number of grid points for visualization.
# DATA SHAPE: Vectors(3,), Matrix(3, 3) for Rank check -> Result(3D Plot).
# MATH: Span = {av1 + bv2 | a,b \in R}. Rank < 3 implies dependence.
# TOOLS: np.meshgrid(), np.linalg.matrix_rank(), self.ax.plot_surface()
# ======================================================================

import numpy as np
import matplotlib.pyplot as plt


class SubspaceVisualizer:
    def __init__(self):
        # Set up a 3D plotting environment
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.first_vector = None
        self.second_vector = None

    def plot_plane(self, first_vector, second_vector):
        """
        Takes two vectors and spans them to show the subspace (plane).
        """
        first_vector = np.asarray(first_vector)
        second_vector = np.asarray(second_vector)

        vectors_matrix = np.array([first_vector, second_vector])
        if np.linalg.matrix_rank(vectors_matrix) < 2:
            print("These vectors are parallel, so they span only a line.")

            scalars = np.linspace(-2, 2, 50)
            line = np.outer(scalars, first_vector)

            self.ax.plot(
                line[:, 0],
                line[:, 1],
               line[:, 2],
                color='blue',
                alpha=0.6,
                label='Span Line'
            )

            self.ax.quiver(0, 0, 0, *first_vector, color='red', label='First Vector')
            self.ax.quiver(0, 0, 0, *second_vector, color='green', label='Second Vector')

            self.first_vector = first_vector
            self.second_vector = second_vector
            return

        # 1. Create a grid of scalars (linear combinations)
        scalars = np.linspace(-2, 2, 10)
        scalar_1, scalar_2 = np.meshgrid(scalars, scalars)

        # 2. Compute the plane: span = a*v1 + b*v2
        x = scalar_1 * first_vector[0] + scalar_2 * second_vector[0]
        y = scalar_1 * first_vector[1] + scalar_2 * second_vector[1]
        z = scalar_1 * first_vector[2] + scalar_2 * second_vector[2]

        # 3. Draw the surface
        self.ax.plot_surface(x, y, z, alpha=0.3, color='blue')

        # 4. Draw the basis vectors as arrows
        self.ax.quiver(0, 0, 0, *first_vector, color='red', label='First Vector')
        self.ax.quiver(0, 0, 0, *second_vector, color='green', label='Second Vector')

        self.first_vector = first_vector
        self.second_vector = second_vector

    def add_vector(self, test_vector):
        """
        Plots a third vector and checks whether it breaks the 2D subspace.
        """
        if self.first_vector is None or self.second_vector is None:
            raise RuntimeError("Call plot_plane() before add_vector().")

        test_vector = np.asarray(test_vector)

        # Plot the test vector
        self.ax.quiver(0, 0, 0, *test_vector, color='gold', label='Test Vector', linewidth=4)

        # Check linear independence using matrix rank
        vectors_matrix = np.array([self.first_vector, self.second_vector, test_vector])
        rank = np.linalg.matrix_rank(vectors_matrix)

        if rank < 3:
            print(f"\nSTATUS: DEPENDENT. Vector {test_vector} lives inside the plane.")
        else:
            print(f"\nSTATUS: INDEPENDENT. Vector {test_vector} breaks out of the plane.")

    def show(self):
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.legend()
        plt.show()


# --- Running the Experiment ---
if __name__ == "__main__":
    viz = SubspaceVisualizer()

    vector_one = np.array([1, 2, 0])
    vector_two = np.array([0, 2, 1])
    viz.plot_plane(vector_one, vector_two)

    # Scenario 1: Redundant vector (a combination of the basis vectors)
    vector_to_test = vector_one + vector_two
    viz.add_vector(vector_to_test)

    # Scenario 2: Independent vector (adds a new dimension)
    # vector_to_test = np.array([0, 0, 5])
    # viz.add_vector(vector_to_test)

    viz.show()