if not set -q MY_ABBR_SET
    set -U MY_ABBR_SET true

    abbr -a bk backup
    abbr -a re restore
    abbr -a mc mkdir-cd
    abbr -a cf create-file
    abbr -a unzip clean-unzip
end