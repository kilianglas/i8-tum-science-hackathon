# General Information

Here are some useful resources for the hackathon challenge. 

# Reading
## TEE
- https://dl.acm.org/doi/full/10.1145/3652597?utm_source=chatgpt.com
    - Good paper about TDX

## SMC
- https://github.com/rdragos/awesome-mpc
    - Contains a lot of pointers and a good starting point in general 
- https://link.springer.com/book/10.1007/978-3-031-12164-7 
    - Good book covering MPC if you are interested in the full background. Can be accessed via TUM login. 
- https://www.escudero.me/pdfs/phd_thesis.pdf 
    - Good PhD thesis that provides a good introduction
- https://eprint.iacr.org/2024/386.pdf
    - Paper covering the MPC framework developed at the chair
-  
# Libraries/ Frameworks
## TEE
- Canonical TDX tools
   - Repo: https://github.com/canonical/tdx
- Dstack:
   - Docs: https://docs.phala.network/overview/phala-network/dstack
   - Github: https://github.com/Dstack-TEE/dstack
   - Developer friendly way to deploy applications in confidential VMs
   - Has local emulation you can use
- Remote attestation
   - https://phala.network/posts/understanding-tdx-attestation-reports-a-developers-guide
   - https://github.com/google/go-tpm-tools 
## SMC
- TensorFlow Federated: 
    - Link: https://www.tensorflow.org/federated
    - Implements federated learning with MPC-based gradient aggregation 
- PySyft
    - Link: https://github.com/OpenMined/PySyft
- The chair's SMC framework: 
    - Docs: https://c.harth-kitzerow.com/mkdocs-hpmpc/
    - Github: 
    - More low-level than e.g., TensorFlow federated. Provides all kinds of primitives to build MPC applications. 
## General Federated Learning
- Flower: 
   - Link: https://flower.ai
   - Could be extended by TEE aggregation
