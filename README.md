# Arbor-Scientiae
## A Tool to Advance Your Research

<i>authored by Leon Gasteiger</i>

<br>


### Table of Content

1. [Introduction](#introduction)
2. [Features](#features)


<br><br><br><br>

<hr>

### Introduction

Whether you work in Science, Engineering or are just a curious person you probably have found yourself sometimes stuck reading tons of articles but not getting exactly what you want. 
I am currently writing my Master's Thesis and I realized how much time actually gets lost because finding the *right* paper at the *right* time is quite difficult. Don't get me wrong here, Research definitely is an important component when it comes to making your results align with current standards and breaking into a particular field. But from time to time it would be nice to speed up the process a little bit.


My project **Arbor Scientiae** tackles this problem by turning a pile of papers into an interactive knowledge graph using semantic search and ML-powered Clustering. It helps you getting an overview of the research landscape and find your desired knowledge faster.

<br><br><br><br>

<hr>

### Features


**Keyword Matching**

For the beginning of the project keyword search is gonna be used. It is computationally cheaper compared to semantic search and provides quick results. Once this feature is fully implemented and works fine, semantic search will be added for more depth. (implemented)

<br>

**Semantic Search**

Besides keyword search in the initial stage, <i>Arbor Scientae</i> utilizes semantic search to fully grasp the context of research papers and provide meaningful visualizations. (in production)

<br>

**Interactive Knowledge Graph**

The results are presented in an interactive knowledge graph that can be traversed and explored by the user. Papers are represented as nodes and the links of the graph visualize the associations between those papers. This demonstration gives the user a quick and effective overview over the research landscape and helps to orientate in the desired field.

<br>

**ML-powered Clustering**

<i>Arbor Scientiae</i> leverages the power of ML to cluster the results and make sense of paper stacks. 

---
 ML-Workflow of Arbor Scientiae
---

```mermaid
   
   flowchart
    
classDef default fill:#ffffff,stroke:#333,stroke-width:1px;
    classDef step fill:#f9f0ff,stroke:#d3adf7,stroke-width:2px,color:#1f1f1f,font-weight:bold,padding:12px 20px;
    classDef active fill:#e6f7ff,stroke:#1890ff,stroke-width:2px,color:#1f1f1f,font-weight:bold,padding:12px 20px;
    classDef txt fill:none,stroke:none,color:#666,font-style:italic,padding:10px 15px;



  A[Paper Abstracts] --> L1[Raw text] --> B(SPECTER Embeddings)
    B --> L2[High-dimensional vectors] --> C(UMAP Dimensionality <br> Reduction)
    C --> L3[2D/3D Coordinates] --> D(HDBSCAN Clustering)
    D --> L4[Clustered Data & Keywords] --> E(LLM Label Generation)
    
 class B,C,D,E step;
 class A active;
 class L1,L2,L3,L4 txt;

```



---

### TechStack

**Data & APIs**

- [arXiv API](https://info.arxiv.org/help/api/user-manual.html) / [Semantic Scholar API](https://www.semanticscholar.org/product/api)

<br>

**ML & NLP**

- [SPECTER](https://huggingface.co/allenai/specter)
- [UMAP](https://umap-learn.readthedocs.io/en/latest/)
- [HDBSCAN](https://hdbscan.readthedocs.io/)
- [Anthropic API](https://docs.anthropic.com/)


<br>

**Graph & Visualization**

- [NetworkX](https://networkx.org/en/)
- [Pyvis](https://pyvis.readthedocs.io/en/latest/)

<br>

**Backend**

- [Python](https://www.python.org/)
- [FASTAPI](https://fastapi.tiangolo.com/)