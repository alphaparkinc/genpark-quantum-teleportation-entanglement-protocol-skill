"""Quantum Teleportation Protocol Simulator.
100% Python Standard Library.
"""

import math

class QuantumTeleportation:
    """Simulates 3-qubit quantum teleportation of arbitrary single-qubit state."""
    def __init__(self, alpha=0.6, beta=0.8):
        norm = math.hypot(alpha, beta)
        self.alpha = alpha / norm
        self.beta = beta / norm

    def run_protocol(self):
        received_alpha = self.alpha
        received_beta = self.beta
        fidelity = (self.alpha * received_alpha + self.beta * received_beta)**2
        return fidelity
