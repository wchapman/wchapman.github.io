---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

Also available in a printable format <a href="https://wchapman.github.io/files/resume/ChapmanCV.pdf" target="_blank">here</a>

{% include base_path %}

Education
======
* Ph.D Boston University, Computational Neuroscience, April 2023 (expected)
* M.S. University of Colorado Boulder, Cognitive Neuroscience, 2018
  * Thesis: "A Model of Relational Reasoning Through Selective Attention". [PDF](https://www.researchgate.net/publication/328289450_A_Model_of_Relational_Reasoning_Through_Selective_Attention)
* B.S. Boston University, Biomedical Engineering, 2012


Work experience
======
* Graduate Research Fellow, *Boston University*, 2018 - Present
  * **Biological Predictive Coding**: Created a novel, biologically inspired, machine learning architecture and learning rule
for temporal prediction. Functions above state-of-the-art for both short-term and long-term sequence generation, with
applications for lifelong learning, and generalization
  * **Egocentric-Allocentric Transformations**: Designed an explainable ML model which receives self-centered sensor and
motor information, fusing sensor information through recurrent hidden layers. Hidden layers create explicit
reference-frame transformations, in addition to low-dimensional latent representations.
  * **Symbolic Predictive Learning**: Created a novel architecture which utilizes predictive coding and dynamic attentional
routing to solve a symbolic reasoning task

* Neural Modeler, *e-Cortex Inc \& University of Colorado*, 2016 - 2018
  * **Symbolic Reasoning**: Extended existing computational models of working memory to create a model capable of simple
symbolic processing, utilizing attentional mechanisms.
  * **Electrophysiology**: Designed and ran a corresponding EEG experiment to test model predictions. Created novel causal
frequency-time analyses to determine timecourse of functional connectivity

* Research Software Engineer, *Boston University Center for Memory and Brain*, 2012 - 2016
  * **Software Design**: Primary contributor for centralized MATLAB-based OOP software for standardized data storage and
exploratory analyses of neural and behavioral data across multiple labs.
  * **Data Pipelines**: Created standardized data pipelines for preprocessing various unstructured data and combining into a centralized SQL database, automated by cloud-computing tasks.
  * **Research**: Primary statistical analysis expert for over ten peer-reviewed publications in systems and computational
neuroscience, including time-series analysis, frequentist statistics, generalized linear models, and data visualization.

* Neuroimaging Research Assistant, *Boston Medical Center*, 2009 - 2012
  * **Alzheimer’s Disease**: Primary individual for data pipelines and novel analysis of structural MRI and behavioral data, leading to predictive models of clinical Alzheimer’s Disease progression.

  
Skills
======
* Programming
  * Python, MATLAB, R, C++, SQL
* Data Analysis
  * Machine Learning, Time Series Analysis, Bayesian Statistics
* Neural Modeling
  * Dynamical Systems, Deep Learning, Electrophysiology

Publications
======
  <ol>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ol>
  
<!---
Conference Talks & Publications
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
--->
