#!/usr/bin/bash

CLEANDIR1="ParallelFiles/ParallelConfigurations-*-*.txt"
EXISTDIR1="ConfigurationAnalysis/"
EXISTDIR2="Output/"
MOVEDIR1="ConfigurationAnalysis/*"
MOVEDIR2="Output/*"
OLDFILES="OldFiles/"

# 2>/dev/null sends errors to another location ->comment out for debugging
#remove old files; if the files are already wiped, send the error to /dev/null
rm $CLEANDIR1 2>/dev/null

#Search if "OldFiles/" exists, else makedir OldFiles
if [ -d "$OLDFILES" ]; then
    continue
else
    mkdir $OLDFILES
fi
#if ConfigurationAnalysis Doesnt exist, then create the dir, else do nothing
if [ -d "$EXISTDIR1" ]; then
    continue
else
    mkdir $EXISTDIR1 2>/dev/null
fi

#if Ouput/ Doesnt exist, then create the dir, else do nothing
if [ -d "$EXISTDIR2" ];then
    continue
else
    mkdir  $EXISTDIR2 2>/dev/null
fi

#Transfer prior data to Old Files to not conflict with the new simulation generation
mv $MOVEDIR1 $OLDFILES 2>/dev/null
mv $MOVEDIR2 $OLDFILES 2>/dev/null

