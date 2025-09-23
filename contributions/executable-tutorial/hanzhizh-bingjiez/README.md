# Assignment Proposal

## Title

Observability with eBPF and FlameGraphs: Profiling Containerized Applications

## Names and KTH ID

- Hanzhi Zhang (hanzhizh@kth.se)  
- Bingjie Zhao (bingjiez@kth.se)

## Deadline

- Task 3  

## Category

- Executable tutorial  

## Description

This executable tutorial demonstrates how to use **eBPF** for observability and performance profiling of containerized applications, combined with **FlameGraph visualization** to identify bottlenecks. Unlike traditional monitoring tools, eBPF allows dynamic tracing at the kernel level with minimal overhead, giving developers deep insights into system and application behavior.  

The tutorial will guide users through the following scenario:

1. **Baseline setup**: Run a simple containerized Python/Flask application and perform a stress test to generate system load.  

2. **Traditional monitoring**: Use `top` and `strace` to show the limitations of conventional tools for observability.  

3. **eBPF tracing**:  
   - Use `bpftrace` and `bcc-tools` to trace syscalls (`execve`, `open`), file I/O, and TCP traffic of the containerized app.  
   - Use `profile` sampling to capture CPU stack traces during load testing.  

4. **FlameGraph visualization**:  
   - Collect profiling data with `perf` or `bpftrace`.  
   - Convert stack traces into folded format and generate an interactive `flamegraph.svg` using Brendan Gregg’s FlameGraph toolkit.  
   - Observe which functions and code paths consume the most CPU time.  

5. **Before vs After comparison**:  
   - Show how traditional monitoring only reveals high-level metrics.  
   - Demonstrate how eBPF + FlameGraph provides deep, actionable insights into performance bottlenecks.  

The tutorial will be delivered on [KillerKoda](https://killercoda.com), using Linux playgrounds that support Docker, bpftrace, and perf tools.  

**Relevance**

Observability and performance profiling are critical aspects of DevOps and Site Reliability Engineering (SRE). This tutorial introduces students to modern, cutting-edge techniques using **eBPF**, which is increasingly adopted in production environments for performance debugging, security, and monitoring.  

By combining eBPF with **FlameGraph visualization**, learners can bridge the gap between raw system-level tracing and intuitive performance insights, aligning with DevOps principles of continuous improvement and operational excellence.
