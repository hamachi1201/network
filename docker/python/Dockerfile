# ベースイメージ
FROM python:3.7

# 依存Pythonライブラリ一覧コピー
COPY etc/supervisor/conf.d/* /etc/supervisor/conf.d/
COPY requirements.txt /opt/requirements.txt

RUN set -x \
  && apt-get update \
  && apt-get upgrade -y --no-install-recommends

# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r /opt/requirements.txt
