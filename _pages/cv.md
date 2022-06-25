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
* Ph.D Boston University, Computational Neuroscience, 2023 (expected)
* M.S. University of Colorado Boulder, Cognitive Psychology, 2018
  * Thesis: "A Model of Relational Reasoning Through Selective Attention". [PDF](https://www.researchgate.net/publication/328289450_A_Model_of_Relational_Reasoning_Through_Selective_Attention)
* B.S. Boston University, Biomedical Engineering, 2012


Work experience
======
* Neural Modeler: 05/2017 - 08/2018
  * e-Cortex Inc
  * Extended existing computational models of working memory to create a model capable of simple symbollic processing, utilizing attentional mechanisms. Designed and ran a corresponding EEG experiment to test model predictions. Created novel causal frequency-time analyses to determine timecourse of functional connectivity.

* Programmer Analyst: 05/2012 - 08/2016
  * Boston University, Center for Systems Neuroscience
  * Primary statistical analysis expert for over ten peer-reviewed publications in systems and comutational neuroscience, including time-series analysis, frequentist statistics, generalized linear models, and data exploration.

* Neuroimaging Research Associate: 05/2009 - 05/2012
  * Boston Medical Center
  * Primary individual for data pipelines and novel analysis of structural MRI and behavioral data, leading to predictive models of clinical Alzheimer's Disease progression.
  
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
