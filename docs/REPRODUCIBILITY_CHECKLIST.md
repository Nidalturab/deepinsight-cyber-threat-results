# Author completion checklist

## Resolve source ambiguities first
- [ ] CICMalDroid20: Table 1 reports 41 features; Section 4.1 reports 470. Confirm actual input feature set and any feature selection.
- [ ] NSL-KDD: Table 1 lists 41 features, while the text describes 3 categorical + 37 numeric + 1 class feature. Confirm predictor columns and exclude the target from predictors.
- [ ] Clarify whether “three fully-connected layers” includes the output layer and specify the complete layer order.

## Data and preprocessing
- [ ] Supply authoritative dataset URLs, release identifiers, filenames, checksums and licenses. Dataset references in the paper are [24] and [25]; no download URLs have been invented here.
- [ ] NSL-KDD: provide KDDTrain+20% and KDDTest+ files and label-to-five-class mapping; verify reported 25,192 / 22,544 counts.
- [ ] CICMalDroid20: supply selected sample IDs, filters, stratified 70/30 split indices and random seed; verify reported 8,118 / 3,480 counts.
- [ ] Supply validation indices (20% of training), stratification and seed.
- [ ] Specify missing-value handling, categorical encoding, scaling, feature order and feature selection.
- [ ] Establish train-only fitting of preprocessing and image layout; document any use of validation/test information.

## DeepInsight
- [ ] Provide implementation/version, image dimensions/channels, embedding method actually used, t-SNE parameters and seed, coordinate mapping, normalization and pixel-collision handling.
- [ ] Provide fitted transformation and feature-to-pixel map.

## Models and training
- [ ] Supply original scripts, dependency lockfile (including TensorFlow/Hyperopt), hardware and deterministic settings.
- [ ] Provide layer sizes/order, convolution filters, kernels, strides, padding, pooling settings, dropout placement and selected dropout values.
- [ ] Provide selected hyperparameters for each dataset/pipeline and Hyperopt trial logs, trial count, search distributions and seeds.
- [ ] Confirm loss function, Xavier initializer variant, Adam parameters, early-stopping patience/min_delta and restore-best-weights behavior.
- [ ] Supply training histories and selected checkpoints.

## Evaluation and release
- [ ] Supply test labels, predictions/probabilities, class order and evaluation script; document F1 averaging and zero-division handling.
- [ ] Recompute Table 4 and Figure 1 from predictions; retain unrounded metrics and confusion matrices.
- [ ] If adding repeated runs, predefine seeds and uncertainty analysis; label these as new experiments.
- [ ] Measure runtime/memory if making quantified overhead claims (not provided in this scaffold).
- [ ] Review attribution, software/data licensing and confidential information before public release.

A complete experiment is not reproducible from the PDF alone. Null configuration values must be resolved from author records, not filled by guessing.
