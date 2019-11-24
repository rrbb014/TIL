# https://computingforgeeks.com/how-to-install-etcd-on-ubuntu-18-04-ubuntu-16-04/
RELEASE="3.2.28"

wget https://github.com/etcd-io/etcd/releases/download/v${RELEASE}/etcd-v${RELEASE}-linux-amd64.tar.gz
tar xvf etcd-v${RELEASE}-linux-amd64.tar.gz
cd etcd-v${RELEASE}-linux-amd64
sudo mv etcd etcdctl /usr/local/bin
etcd --version

wait 
sudo mkdir -p /var/lib/etcd/
sudo mkdir /etc/etcd

sudo groupadd --system etcd
sudo useradd -s /sbin/nologin --system -g etcd etcd

sudo chown -R etcd:etcd /var/lib/etcd

echo "Go https://computingforgeeks.com/how-to-install-etcd-on-ubuntu-18-04-ubuntu-16-04/"
echo "and configure etcd3"
