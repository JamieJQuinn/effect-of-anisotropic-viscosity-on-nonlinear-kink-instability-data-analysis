#!/usr/bin/env bash
ISOTROPIC_DIR=/nas/1101974q/archie-latest-organisation-sept-2018/kink-instabilities/initially-unstable/cadence-5-v1e-4r5e-4.5/v1e-4r5e-4.5-isotropic
SWITCHING_DIR=/nas/1101974q/archie-latest-organisation-sept-2018/kink-instabilities/initially-unstable/cadence-5-v1e-4r5e-4.5/v1e-4r5e-4.5-switching
#ls ${ISOTROPIC_DIR}/Data/*.sdf ${SWITCHING_DIR}/Data/*.sdf | sed -e 's/ /\\n/g' > filename_list

echo ${ISOTROPIC_DIR}/Data/0009.sdf | sed -e 's/ /\\n/g' > filename_list
echo ${ISOTROPIC_DIR}/Data/0010.sdf | sed -e 's/ /\\n/g' >> filename_list
echo ${ISOTROPIC_DIR}/Data/0035.sdf | sed -e 's/ /\\n/g' >> filename_list
echo ${SWITCHING_DIR}/Data/0035.sdf | sed -e 's/ /\\n/g' >> filename_list

ISOTROPIC_DIR=/nas/1101974q/archie-latest-organisation-sept-2018/kink-instabilities/initially-unstable/long-run-cadence-5-v1e-4r5e-4.5/v1e-4r5e-4.5-isotropic
SWITCHING_DIR=/nas/1101974q/archie-latest-organisation-sept-2018/kink-instabilities/initially-unstable/long-run-cadence-5-v1e-4r5e-4.5/v1e-4r5e-4.5-switching
#ls ${ISOTROPIC_DIR}/Data/*.sdf ${SWITCHING_DIR}/Data/*.sdf | sed -e 's/ /\\n/g' >> filename_list

echo ${ISOTROPIC_DIR}/Data/0062.sdf | sed -e 's/ /\\n/g' >> filename_list
echo ${SWITCHING_DIR}/Data/0059.sdf | sed -e 's/ /\\n/g' >> filename_list
