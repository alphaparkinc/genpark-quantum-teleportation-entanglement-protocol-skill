from client import QuantumTeleportation

tp = QuantumTeleportation(alpha=0.8, beta=0.6)
fid = tp.run_protocol()
print(f"Teleportation completed with state fidelity: {fid:.4f}")
