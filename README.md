<p align="center">
  <img src="assets/subspace-banner.png" 
       alt="Linear Algebra Subspace Banner"
       style="width: 100%; max-width: 100%; height: 250px; display: block; object-fit: cover; object-position: center; border-radius: 10px;">
</p>

# Linear Algebra & NumPy: AI Foundations

> **Status:** Active Study 
> **Focus:** Mathematical Foundations for Deep Learning

## 📖 Project Overview
This repository documents my progression through the mathematical concepts essential for Artificial Intelligence and Machine Learning. The goal is to move beyond high-level libraries and understand the low-level linear algebra operations that drive modern neural networks.

I am utilizing **Python** and **NumPy** to implement these concepts manually, bridging the gap between abstract mathematical theory and executable code.

## 🛠 Tech Stack & Tools
* **Language:** Python 3.x
* **Core Library:** NumPy (for vectorization and matrix manipulation)
* **Visualization:** Matplotlib / Seaborn
* **Environment:** Jupyter Notebooks (Anaconda)

## 📂 Repository Structure

### `01-Course-Notes/`
**Primary Resource:** *Master Linear Algebra: Theory and Implementation in Code* (Mike X Cohen)
* **Detailed code-along notebooks:**
  * Vectors & Spaces (Dot products, spans, basis vectors)
  * Matrix Operations (Multiplication, Inverse, Rank)
  * Eigendecomposition & SVD
  * Least Squares & Projections
* **Vectors & Spaces:**
  * **The Span:** Deep dive into the infinite reach of linear combinations.
  * **Algorithmic Verifier:** Developed a custom Python tool using `np.linalg.matrix_rank` to programmatically validate subspace membership. This ensures that any target vector is mathematically "reachable" before proceeding with downstream model transformations.

### `02-Experiments/`
* **My own sandbox for testing concepts:**
  * Independent challenges and implementations of algorithms from scratch without relying on pre-built solver functions.
* **3D Subspace Visualization Engine:**
  * Developed a coordinate-projection tool to visualize how basis vectors define a 2D subspace within 3D space.
  * Implemented cross-product normal calculations to render infinite planes using `np.meshgrid` and `plot_surface`.
  * Integrated axis-limit constraints and camera-angle adjustments to ensure clear spatial orientation of vector-plane relationships.

## 🚀 Why This Matters for AI
Understanding these concepts is critical for:
* **Dimensionality Reduction** (PCA, SVD)
* **Data Transformation** (Basis changes, Linear mappings)
* **Optimization** (Gradient descent landscapes)

---
*Author: Josh Hasam*
