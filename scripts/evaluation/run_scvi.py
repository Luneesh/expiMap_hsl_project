import scanpy as sc
import argparse
import scvi

parser = argparse.ArgumentParser()

parser.add_argument("adata_file")
parser.add_argument("batch_col")

args = parser.parse_args()

adata_file = args.adata_file
batch_col = args.batch_col

print(adata_file, batch_col)

adata = sc.read(adata_file)

scvi.data.setup_anndata(adata, batch_key=batch_col)

vae = scvi.model.SCVI(adata)
vae.train(max_epochs=500, early_stopping=True)

adata.obsm["X_scvi"] = vae.get_latent_representation()

adata.write(adata_file)
