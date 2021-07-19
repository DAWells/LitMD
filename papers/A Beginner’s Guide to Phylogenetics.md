# A Beginner’s Guide to Phylogenetics
## 2013
## Roy D. Sleator
### tags
phylogenetics
###tags

Distance based trees includ neighbour joining, weighted neighbout joining, and minimum evolution (and the similar Fitch Margoliash). Minimum evoltuion and FM are  the best of the distance methods but considerably slower.
Weighted neighbour joining assigns less weight to longer distances in the distance matrix which helps to reduce the affects of long branch attraction.

Character based methods include: maximum parsimony, maximum likelihood, and bayesian approaches. Maximum parsimony is strongly affected by its assumption of constant evolutionary rates. ML approaches can use likelihood to perform statistical tests but they are computationally intensive.

In reality distance and character based methods tend to be used concurrently, with distance trees being used initially to test model parameters and the best model being used to find the ML tree.

Once an optimum tree has been chosen support for internal clades must be quantified. Bootstrapping is commonly used. In phylogenetics non-parametric bootstrapping resamples the taxa and >70\% is usually interpreted as "true". Parametric bootstrapping uses numerical simulation and is commonly applied to compare competing hypotheses. Posterior probabilities are sometimes used to assess support for a given tree.

Major issues for phylognetics are saturation (where sequences are differ due to multiple mutations at the same site), long branch attraction (where long branches are incorrectly grouped together), and lateral gene transfer (effectivel, where the evolutionary distance between taxa varies across the genome).
