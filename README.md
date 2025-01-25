# HierTKG: Hierarchical Temporal Knowledge Graph for Rumor Detection

## Abstract
The rapid spread of misinformation on social media, especially during crises, challenges public decision-making. To address this, we propose **HierTKG**, a novel framework that integrates **Temporal Graph Networks (TGN)** with **hierarchical pooling (DiffPool)** to model rumor dynamics across temporal and structural scales. HierTKG captures key propagation phases, enabling improved temporal link prediction and actionable insights for misinformation control.

Our experiments demonstrate the effectiveness of HierTKG, achieving an MRR of **0.9845** on ICEWS14 and **0.9312** on WikiData, with strong performance even on noisy datasets like PHEME (MRR: **0.8802**). By modeling structured event sequences and dynamic social interactions, HierTKG adapts to diverse propagation patterns, offering a scalable and robust solution for real-time analysis and prediction of rumor spread.

## Key Contributions
- **Temporal Knowledge Graph Construction**  
  Developed a comprehensive temporal knowledge graph from the PHEME dataset, capturing nuanced temporal and relational information critical for understanding rumor propagation.

- **HierTKG Framework**  
  Introduced an innovative integration of **TGN** and **DiffPool**, modeling both temporal evolution and hierarchical structure of knowledge graphs for enhanced insights.

- **Enhanced Temporal Link Prediction**  
  Our approach improves the accuracy of predicting rumor spread by incorporating multi-scale structural and temporal dynamics.

- **Comprehensive Evaluation**  
  Extensive experiments, including ablation studies, validate the framework's effectiveness and robustness using datasets such as ICEWS14, WikiData, and PHEME.

## Problem Definition
We address the problem of **link prediction** in temporal knowledge graphs (TKGs) by constructing a **Hierarchical Temporal Knowledge Graph (HierTKG)** that captures both temporal and structural information. Our goal is to predict future interactions based on historical patterns by estimating the likelihood of future links.

### Mathematical Formulation
Given a temporal knowledge graph \( G = \{G_1, G_2, ..., G_T\} \), our objective is to predict future links for entities at \( t > T \). We achieve this by learning a scoring function \( f \) that takes node embeddings, relation types, and timestamps as inputs, using a binary cross-entropy loss to train the model.

## Framework Overview
HierTKG consists of three key modules:

1. **Graph Construction**  
   - Temporal knowledge graph construction based on relational and temporal dependencies.

2. **HierTKG Algorithm**  
   - **TGN Processing** for capturing evolving interactions over time.
   - **DiffPool Processing** for hierarchical node clustering and representation learning.
   - **Fusion Layer** combining temporal and structural embeddings with attention mechanisms.

3. **Output**  
   - The model outputs link predictions for downstream misinformation mitigation tasks.

![HierTKG Framework](image.png)

## Algorithm
The link prediction process in HierTKG follows these steps:

1. Initialize TGN memory and hierarchical structure.
2. Process temporal embeddings and node interactions using TGN.
3. Apply hierarchical pooling via DiffPool.
4. Fuse temporal and structural embeddings using multi-head attention.
5. Compute link predictions and update model parameters via gradient descent.

## Experimental Results
HierTKG's performance was evaluated using the following datasets:

| Dataset   | AP     | MRR   |
|-----------|--------|-------|
| ICEWS14   | 0.9708 | 0.9845 |
| ICEWS18   | 0.9479 | 0.9646 |
| WikiData  | 0.8627 | 0.9312 |
| PHEME     | 0.6918 | 0.8802 |

HierTKG outperforms existing models such as SPA and TLT-KGE by effectively handling hierarchical and temporal dependencies, making it well-suited for datasets with strong latent structures like ICEWS14.

## Challenges and Insights
- **Social Media Noise**  
  PHEME data poses challenges due to incomplete information and informal language, requiring advanced aggregation and filtering techniques.

- **Hierarchical Aggregation**  
  DiffPool enhances feature aggregation, allowing the model to emphasize critical relationships while reducing noise.

- **Model Interpretability**  
  Multi-head attention improves model explainability, highlighting key dependencies in rumor propagation.

## Baseline Comparisons
HierTKG surpasses baseline models such as SPA (2022) and TLT-KGE (2022), which struggle with evolving social cyber threats. Competing approaches like EmtE (2024) and TIE (2024) effectively handle temporal data but lack hierarchical aggregation, limiting their effectiveness in structured datasets.

## Citation
```css
@article{HierTKG2024,
  author    = {Your Name},
  title     = {HierTKG: Hierarchical Temporal Knowledge Graph for Rumor Detection},
  year      = {2024},
  journal   = {Arxiv},
}
```
## Installation
To install and run the project:

```bash
git clone https://github.com/your-repo/hiertkg.git
cd hiertkg
pip install -r requirements.txt
