> [!Info]
> Topic 04, **Memory Components and Organization**, focuses on how a computer system stores data, the hierarchy of different storage types, and the complex mechanisms used to bridge the speed gap between the CPU and main memory.

# 1. Types of Memory

Computer memory is categorized into primary and secondary storage, each with distinct technologies and purposes.

- **Primary Memory:** This is the memory directly accessible by the CPU.
    - **RAM (Random Access Memory):** Volatile memory used for temporary storage while the computer is running.
        - **SRAM (Static RAM):** Used for cache; it is very fast but expensive.
        - **DRAM (Dynamic RAM):** Used for main memory; it is slower than SRAM but more affordable.
    - **ROM (Read Only Memory):** Non-volatile memory used for permanent storage.
        - **PROM:** Programmable ROM.
        - **EEPROM:** Electrically Erasable Programmable ROM.
- **Secondary Memory:** Used for long-term storage, including Magnetic Disks (HDD), Magnetic Tapes, and USB sticks.
- **Flash Memory and SSDs:** **Flash memory** is non-volatile and used in memory cards and USB drives. **Solid State Drives (SSDs)** are typically based on flash memory and offer faster access times and better physical resistance than HDDs, though they can deplete charge over time without power.

# 2. The Memory Hierarchy and the CPU-Memory Gap

Memory is organized into a hierarchy based on **access time (latency), cost, size, and distance from the CPU**.

- **The Hierarchy:** At the top are **Processor Registers** (fastest, smallest, most expensive), followed by **Cache**, **Main Memory (RAM)**, **Flash/USB memory**, **Hard Drives**, and finally **Tape Backup** (slowest, largest, cheapest).
- **The CPU-Memory Gap:** While CPU speed increases rapidly, memory access times cannot match this pace. To bridge this performance bottleneck, systems rely on the **Principle of Locality**.

# 3. Principle of Locality

This is the tendency of the CPU to access the same set of memory locations repeatedly over short periods.

- **Spatial Locality:** Items with nearby addresses tend to be referenced close together in time.
- **Temporal Locality:** Recently referenced items are likely to be referenced again in the near future.

# 4. Cache Memory

**Cache** is a small, fast, and transient memory space residing on the CPU chip that keeps copies of data from the larger, slower main memory.

**Cache Write Policies**

Maintaining consistency between the cache and main memory is a challenge when data is altered.

- **Write Through:** Every write operation happens synchronously on both the cache and main memory. It is simple but increases bus traffic.
- **Write Back:** Writes occur only in the cache. Data is only written to main memory when it is evicted (replaced) from the cache.

## Mapping Schemes

Since the cache is smaller than main memory, a mapping scheme is required to determine where data is stored. Data is transferred in fixed-size blocks called **Cache Lines**.

- **Direct Mapped Cache:** Each memory block maps to exactly one pre-defined cache entry position. Because multiple memory blocks map to the same spot, a **Tag** is used to identify which address is currently stored. An address is broken into three parts:
    - **Offset:** Identifies the exact unit within a cache line.
    - **Index:** Specifies which cache entry the data belongs to.
    - **Tag:** Used to verify if the stored data matches the requested address.
- **Set Associative Cache:** Memory blocks are mapped to a **Set** rather than a single entry. For example, in a **2-way set associative cache**, a set can hold two different cache lines.
- **Replacement Policies:** When a set is full and new data must be brought in, a **replacement policy** determines which entry to evict (e.g., based on locality).

# 5. Virtual Memory

According to the syllabus, this topic also covers **Virtual Memory**, which includes:

- **Paging and Segmentation:** Methods for dividing memory to manage it efficiently.
- **Address Translation:** The process of converting virtual addresses (used by programs) into physical addresses (actual hardware locations). This is handled by the **Memory Management Unit (MMU)**.
- **Memory Fragmentation:** Issues that arise when memory is allocated and deallocated, leaving small, unusable gaps.

*Note: While Virtual Memory and performance measurement are listed in the syllabus, detailed lecture slides for these specific sub-topics were not included in the provided excerpts beyond the role of the MMU*.

---
# Lecture Notes
![[IS1202 Lecture 4.1.pdf]]