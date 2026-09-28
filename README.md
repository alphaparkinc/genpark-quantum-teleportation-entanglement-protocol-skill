# Quantum Teleportation Protocol Skill

High-efficiency, zero-dependency Python implementation of the **3-Qubit Quantum Teleportation Protocol**.

## Features
- **Bell-State Shared Entanglement**: Distributes shared EPR pair \((|\Phi^+angle)\) between Alice and Bob.
- **Bell Measurement & Feedforward**: Encodes quantum information into 2 classical bits followed by Pauli \(X^a Z^b\) correction.
- **Zero External Dependencies**: Pure Python standard library (`math`).
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
sequenceDiagram
    participant Alice
    participant EPRSource as Bell Pair Source
    participant Bob

    EPRSource->>Alice: Qubit 1 (|Phi+>)
    EPRSource->>Bob: Qubit 2 (|Phi+>)
    Note over Alice: Alice holds target Qubit 0 (psi)
    Alice->>Alice: Bell Basis Measurement on (0, 1)
    Alice->>Bob: 2 Classical Bits (m0, m1)
    Note over Bob: Apply Pauli Correction X^(m1) Z^(m0)
    Note over Bob: Reconstructed State (psi) with Fidelity 1.0
```
