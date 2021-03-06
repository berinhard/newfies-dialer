#!/bin/bash
#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

#
# To download and run the script on your server :
# cd /usr/src/ ; rm install-all.sh ; wget --no-check-certificate https://raw.github.com/Star2Billing/newfies-dialer/master/install/install-all.sh ; chmod +x install-all.sh ; ./install-all.sh
#

BRANCH='master'

# Identify Linux Distribution type
func_identify_os() {

    if [ -f /etc/debian_version ] ; then
        if [ "$(lsb_release -cs)" != "precise" ]; then
            echo "This script is only intended to run on Ubuntu 12.04 TLS"
            exit 1
        fi
    else
        echo ""
        echo "This script is only intended to run on Ubuntu 12.04 TLS"
        echo ""
        exit 1
    fi
}

#Identify the OS
func_identify_os

echo ""
echo "> > > This is only to be installed on a fresh new installation of Ubuntu 12.04 TLS! < < <"
echo ""
echo "It will install Newfies-Dialer and Freeswitch on your server"
echo "Press Enter to continue or CTRL-C to exit"
echo ""
read TEMP


apt-get -y update
apt-get -y install vim git-core

#Install Freeswitch
cd /usr/src/
wget --no-check-certificate  https://raw.github.com/Star2Billing/newfies-dialer/$BRANCH/install/install-freeswitch.sh -O install-freeswitch.sh
bash install-freeswitch.sh
/etc/init.d/freeswitch start

#Install Newfies
cd /usr/src/
wget --no-check-certificate https://raw.github.com/Star2Billing/newfies-dialer/$BRANCH/install/install-newfies.sh -O install-newfies.sh
bash install-newfies.sh
