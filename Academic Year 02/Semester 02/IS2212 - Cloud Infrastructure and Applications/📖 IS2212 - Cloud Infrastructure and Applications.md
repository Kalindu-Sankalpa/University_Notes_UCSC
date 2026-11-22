- **Course Code** : IS2212
- **Course Name** : Cloud Infrastructure and Applications
- **Lecturers** : Kenneth Thilakarathna & Dilanga Harshani (UCSC)

#Lesson-Plan 

> [!important] Goal
> This course traces the architectural and operational evolution of enterprise IT—following a retail enterprise's real-world transition from traditional on-premises datacenters, through server virtualization, to modern cloud-native infrastructures. Students master distributed computing foundations, cloud service models (IaaS, PaaS, SaaS), elasticity, infrastructure automation, and resilient cloud architecture.

---

# The specific objectives of the module include:

- **Traditional Datacenter Architecture & Limitations:** Deconstructing facilities (TIA-942), computing, storage (SAN/NAS), networking fabrics, and analyzing the financial and operational trade-offs of fixed-capacity planning (CapEx vs OpEx).
- **Virtualization & Hypervisor Mechanics:** Evaluating Type 1 (bare-metal) and Type 2 (hosted) hypervisors, container-level virtualization, server consolidation economics, and hardware abstraction boundaries.
- **Foundations & Core Characteristics of Cloud Computing:** Understanding the NIST SP 800-145 definition and the six core cloud characteristics (on-demand self-service, ubiquitous access, multitenancy, rapid elasticity, measured service, resiliency).
- **Cloud Delivery & Service Models:** Analyzing IaaS, PaaS, and SaaS stacks, ownership boundaries, the shared responsibility model, and strategic migration trade-offs.
- **Scalability, Resilience & Cloud Mindset:** Differentiating vertical scaling (scale-up) from horizontal scaling (scale-out), architectural statelessness, and shifting from procurement to service-oriented operations.

---

# Topic Covered

### Part 1: Datacenter Foundations, Virtualization & Service Models

1. [[Life in the Datacenter]]
	- **The Retailer Case Study:** The Black Friday traffic surge, server saturation, and systemic outage mechanics.
	- **The Three Datacenter Layers:** Facilities (power, UPS, cooling, fire suppression, TIA-942), Hardware (servers, SAN/NAS, switches, routers), and Software.
	- **Operational Realities & The Dev/Ops Wall:** Siloed organizational teams, ticket-driven handoffs, and release friction.
	- **Capacity Planning & Economics:** Forecasting demand years in advance, CapEx vs OpEx, and the mathematical cost of idle vs insufficient capacity.
	- **Intermediary Solutions:** Colocation, managed hosting, and traditional outsourcing ownership matrices.

2. [[From Virtual Machines to the Cloud]]
	- **Virtualization Fundamentals:** Hardware abstraction, hypervisors, server consolidation economics, and resource replication.
	- **Virtualization Taxonomy:** Type 1 (Bare-Metal) vs Type 2 (Hosted) vs OS-level Containerization (Docker/Kubernetes).
	- **The Limits of Virtualization:** What hypervisors solved vs what remained broken (lack of self-service, fixed host pools, upfront CapEx).
	- **Defining Cloud Computing:** The NIST SP 800-145 framework and the six cloud characteristics.
	- **Scaling Architectures:** Vertical scaling (Scale Up) vs Horizontal scaling (Scale Out) trade-offs.
	- **The Mindset Revolution:** Shifting from IT procurement to dynamic cloud service consumption ("thinking in the first derivative").

3. [[Cloud Service Models]]
	- **Cloud Roles & Relationships:** Cloud Provider, Cloud Consumer, Cloud Broker, Cloud Service Owner, and Cloud Resource Administrator.
	- **Trust & Organizational Boundaries:** Overlapping trust zones in multi-tenant cloud environments.
	- **The 7-Layer Application Stack:** Facilities, storage/network, virtualization, OS, runtime, data, and application.
	- **The Shared Responsibility Model:** "Who manages what?" across On-premises, IaaS, PaaS, and SaaS ("Data is always the customer's concern").
	- **Deep-Dive into IaaS, PaaS, and SaaS:** Technical capabilities, consumer decisions, benefits, trade-offs, and enterprise retailer fit.
	- **Control vs. Convenience:** The fundamental trade-off spectrum and multi-model service composition.

4. [[Cloud Deployment Models]]
	- **The Four Deployment Models:** Public, Private, Multicloud, Community, and Hybrid cloud taxonomies and trade-offs.
	- **The Governance Axiom:** Service models define what you rent; deployment models define where and for whom.
	- **Physical Cloud Topology:** Global Regions, Availability Zones (AZs), and Edge Locations / CDN caching points.
	- **Hybrid Cloud Mechanics & Cloud Bursting:** Legacy inertia, low-latency factory/warehouse edge needs, and the hybrid operational tax.
	- **Architectural Reality (Stage vs. Destination):** Phased transitional stepping stone vs. permanent hybrid equilibrium.
	- **System-First Decision Framework:** Kavis 4-step discovery methodology, the 6 driving decision criteria, and rule-of-thumb flowchart.
	- **Multi-Criteria Weighted Scoring Matrix:** Mathematical evaluation model ($\sum w_i \times s_i$) and the Retailer Payroll worked case study.
	- **Real-World Case Study (NOAA):** Rapid 25,000-user government SaaS migration analysis (Pressure, Removed, Not Solved).
	- **Strategic Enterprise Workload Placement:** Architectural mapping for web shop, inventory, payroll, payments, analytics, and photo storage.

---

# IS2212 Syllabus

![[IS2212 - Syllabus.pdf]]
