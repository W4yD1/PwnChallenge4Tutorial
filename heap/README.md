# Heap Challenges

This folder contains three heap exploitation challenges for CTF PWN competitions:

## 1. Fast Bin Attack (`fastbin_attack/`)

**Vulnerability**: Fast bin double free and manipulation  
**Target Environment**: Ubuntu 18.04 with glibc 2.27  
**Difficulty**: Intermediate

This challenge demonstrates classic fast bin exploitation techniques. Players need to:
- Allocate chunks in fast bin size range (≤0x80 bytes)
- Exploit use-after-free to manipulate fast bin linked list
- Achieve arbitrary allocation to gain code execution

**Key Learning Points**:
- Fast bin mechanism in glibc heap management
- Double free detection bypass
- Fast bin linked list corruption

## 2. Off by One (`off_by_one/`)

**Vulnerability**: Off-by-one byte overflow  
**Target Environment**: Ubuntu 20.04 with glibc 2.31  
**Difficulty**: Intermediate

This challenge focuses on off-by-one vulnerabilities in heap context. Players need to:
- Understand heap chunk layout and metadata
- Exploit the extra byte write to corrupt adjacent chunk headers
- Use corrupted metadata to achieve arbitrary write

**Key Learning Points**:
- Heap chunk metadata structure
- Off-by-one exploitation techniques
- Heap consolidation and coalescing

## 3. Tcache Poison (`tcache_poison/`)

**Vulnerability**: Use-after-free enabling tcache poisoning  
**Target Environment**: Ubuntu 22.04 with glibc 2.35  
**Difficulty**: Intermediate-Advanced

This challenge explores modern heap exploitation using tcache. Players need to:
- Free chunks to populate tcache bins
- Exploit use-after-free to corrupt tcache next pointers
- Achieve arbitrary allocation through tcache poisoning

**Key Learning Points**:
- Tcache mechanism introduced in glibc 2.26+
- Tcache poisoning attack vectors
- Modern heap exploitation techniques

## Usage

Each challenge can be built and deployed using Docker:

```bash
cd heap/<challenge_name>
docker build -t <challenge_name> .
docker run -p 70:70 <challenge_name>
```

Connect to the challenge using netcat:
```bash
nc localhost 70
```

## Challenge Structure

Each challenge follows the same structure:
- Interactive menu system with allocate/free/edit/show operations
- Win function that spawns shell when successfully exploited
- Address information provided to assist exploitation
- Safety limits on allocation sizes and chunk counts