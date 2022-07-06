# Methodology

- Lets keep the input vector and key constant 
  (lets try with changing the key or input vector is a possibility if initial results are promising)

- Input data: encrypted data of fixed size each bit of an input represented as a float, labels: Original text (each bit encrypted as a float)

- Measure how good are we doing by counting correct bits in the output and comparing that to a random distribution

## First steps
As a first step we collect information needed to fully understand the topic.
- Prepare required tools and repositories
- Create wiki for our research 
- Collect links to used papers in [sources.md](sources.md) database
- Created simplified [crypto library](crypto/_innit_.py) to abstract external libraries implementation details
- Check our methodology on a simpler encryption algorithm (`DES`) 
- Investigate the concept of spiking nn and try to follow simple examples from `ssn-torch`
- Investigate challenges AES poses, the mathematics laying behind AES protocol

## Next steps
- Investigation of different possible ways to convert our dataset into the form appropriate for SNN
- First SNN implementation attempts for DES
- First NN implementation for AES
- Investigate NN comparison methods, in order to compare trained neural networks repetable tests are needed,
and tools to interpret results of tests made
  