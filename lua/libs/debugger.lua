--
-- Newfies-Dialer License
-- http://www.newfies-dialer.org
--
-- This Source Code Form is subject to the terms of the Mozilla Public
-- License, v. 2.0. If a copy of the MPL was not distributed with this file,
-- You can obtain one at http://mozilla.org/MPL/2.0/.
--
-- Copyright (C) 2011-2013 Star2Billing S.L.
--
-- The Initial Developer of the Original Code is
-- Arezqui Belaid <info@star2billing.com>
--

package.path = package.path .. ";/usr/share/newfies-lua/?.lua";
package.path = package.path .. ";/usr/share/newfies-lua/libs/?.lua";

-- local oo = require "loop.base"
local oo = require "loop.simple"
require "logging.file"

local LOGDIR = '/usr/share/newfies-lua/'
local logger = logging.file(LOGDIR .. "logs_%s.log", "%Y-%m-%d")

-- Set Logging Level
-- logging.DEBUG
-- The DEBUG level designates fine-grained informational events that are most useful to debug an application.
-- logging.INFO
-- The INFO level designates informational messages that highlight the progress of the application at coarse-grained level.
-- logging.WARN
-- The WARN level designates potentially harmful situations.
-- logging.ERROR
-- The ERROR level designates error events that might still allow the application to continue running.
-- logging.FATAL
-- The FATAL level designates very severe error events that would presumably lead the application to abort.
--
logger:setLevel(logging.DEBUG)


Debugger = oo.class{
    -- default field values
    fs_env = false,
    -- verbosity_level : DEBUG, INFO, WARN, ERROR
    -- DEBUG - The DEBUG Level designates fine-grained informational
    --         events that are most useful to debug an application.
    -- INFO – The INFO level designates informational messages that
    --        highlight the progress of the application at coarse-grained level.
    -- WARN – The WARN level designates potentially harmful situations.
    -- ERROR – The ERROR level designates error events that might still
    --         allow the application to continue running.
    verbosity_level = 'INFO',
}

function Debugger:__init(verbosity_level, fs_env)
    -- self is the class
    return oo.rawnew(self, {
        verbosity_level = verbosity_level,
        fs_env = fs_env,
    })
end


function Debugger:msg(level, message)
    -- level : DEBUG, INFO, WARN, ERROR
    if not self.fs_env then
        print(message)
    else
        freeswitch.consoleLog(level, message.."\n")
    end
    if level == 'DEBUG' then
        logger:debug(message)
    elseif level == 'INFO' then
        logger:info(message)
    elseif level == 'WARN' then
        logger:warn(message)
    elseif level == 'ERROR' then
        logger:error(message)
    end

end

