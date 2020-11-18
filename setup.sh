#!/bin/bash
readonly PROCNAME=${0##*/}
function log() {
  local fname=${BASH_SOURCE[1]##*/}
  echo "$(date '+%Y-%m-%dT%H:%M:%S') ${PROCNAME} (${fname}:${BASH_LINENO[0]}:${FUNCNAME[1]}) $@"
}

log "INFO:pythonのセットアップを始めます"
log "INFO:pyenvを始めます"
python -m venv env
log "INFO:websocketをpip installします"
pip install websockets==8.1
log "INFO:paramikoをpip installします"
pip install paramiko==2.7.2
log "INFO:cspをinstallします"
pip install scp==0.13.3
log "INFO:install済モジュールを表示します"
pip freeze
log "INFO:pythonのセットアップを終了します"
