import pulumi
import pulumi_civo as civo

# Create a credential for the object store with a specific access key and secret key
obj_store_cred = civo.ObjectStoreCredential("my-creds-87878", region="LON1")

obj_store = civo.ObjectStore("pulumi-state",
                             access_key_id=obj_store_cred.access_key_id,
                             max_size_gb=500,
                             region="LON1")

pulumi.export('obj_store_id', obj_store.id)
pulumi.export('obj_store_url', obj_store.bucket_url)
pulumi.export('obj_store_name', obj_store.name)

#web_server = civo.Instance("web-server", region="LON1", disk_image="ubuntu-jammy")
