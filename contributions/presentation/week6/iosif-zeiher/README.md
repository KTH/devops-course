# Assignment Proposal

## Title

Using Cross Monitoring to scale on the Edge

## Names and KTH ID

  - Iosif Koen (iosif@kth.se)
  - Fabian Zeiher (zeiher@kth.se)

## Deadline

- Week 6

## Category

- Presentation

## Description

Computing power on edge devices is usually limited. Therefore scaling on the edge is quite difficult.
The [A Design of Serverless Computing Service for Edge Clouds](./A_Design_of_Serverless_Computing_Service_for_Edge_Clouds.pdf) proposes an approach to scale workloads on the edge without using a cload
or otherwise centralized infrastructure. Utilising serverless principles workloads can be moved between edge nodes.
In order to detect which nodes are overloaded we need a monitoring approach. Again, we do not want
to relay on a centralized monitoring server, therefore we employ _cross monitoring_ where edge
nodes scrape data directly from their neighbors in order to monitor CPU load, network trafic and other metrix.

We have already provided a rough draft of our slides, here: [WIP Slides](./WIP-slides.pdf) 

**Relevance**

DevOps on the edge poses special challenges and requires sepecialised solutions.
The domain of edge computing is quickly gaining relevance as industries digitalise there production lines.
