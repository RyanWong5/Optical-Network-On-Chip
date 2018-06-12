commit 3d0d573ca2254609af6dfa216050b6c9d4857bc8
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Tue Jun 12 14:53:14 2018 -0500

    Removing *.zip files

commit 7d95a89bc3cfd596e242e644c59ecf537bb7f6f9
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Tue Jun 12 13:36:38 2018 -0500

    Edit .gitignore to ignore Ouptut files

commit b72b484c5f802e05bafd937dbe4cdb9846ad2b6d
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Tue Jun 12 13:35:04 2018 -0500

    ReGenerated 60k/120k Configurations adding node 16

commit 745f0a12ce0622ce4bf0e3b1a6402999a5566394
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 21:22:46 2018 -0500

    Converting Configuration text files to unix using dos2unix

commit 7cf53c2009e023ba0d6f8a5408a79668d9e9308a
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 21:09:09 2018 -0500

    Fixed work partitioning, at least for 5 config and up to 4 nodes, will retry when larger cluster becomes available

commit 5b24b67743d5605b019c62783588ed29749e3069
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 15:16:47 2018 -0500

    Fixed the * being generated due to duplicate naming

commit 8b0375595c46658db924018ae873e1dbea6cee8d
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 15:01:19 2018 -0500

    fixing shell script

commit b7dd2e398539687e1289935d95294903d9cfe6d8
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 14:42:30 2018 -0500

    Changed folder to dir

commit cd5ed8e65e1942c1df6b92309293372b3af3f51f
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 14:40:20 2018 -0500

    fixed shellscript to send mv errors to another location

commit b8b3d9ab73394df018463cdd9dd70e32f2c05b43
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 14:08:44 2018 -0500

    fixed outfile filename generation

commit cecaa1accc659d2754c67c3e17b299cf9efd1167
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 12:31:01 2018 -0500

    added shell script to now generate the simulation environment with the required folders

commit 3292fc8c263466bcef62f2bce3bbd681d4696218
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 11:58:34 2018 -0400

    update gitignore

commit 63123c2af8672617a39065e14944b919d5fd829f
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Mon Jun 11 11:57:53 2018 -0400

    Work Partioning function written, now need to test

commit 8e1b1a41dd1e35bb0b71c695940b4c4aa12f6c74
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 22:14:36 2018 -0500

    re-ignoring output + ConfigAnalysis

commit c2ea5537e534152146994d1437ef01973899adf4
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 22:13:55 2018 -0500

    Cleaning .txt files from output and configanalysis

commit 5514345b359baa12337b6b8c55854ac55c8fd083
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 22:11:44 2018 -0500

    changed source code to SourceCode

commit c4eb7f9c68dfdc39556d574158a21704f6c0c18e
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 22:09:40 2018 -0500

    Fixed Argument passing, next step work partitioning and hostfile generation

commit 2cbd02beea8f4e6902142948fc9ef4efd07aeadc
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 21:02:57 2018 -0400

    Fixed file naming system and created def to parse the configuration argument

commit 09b00f9ee30d81c41d20ab64bf046d851926e822
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 20:44:29 2018 -0400

    Set the variable 'theConfigurationFile' which was unset if the config file was not in the same dir as the benchmarks....

commit 1192a952f50b09103fc6598f1f22435586fa834b
Author: Ryan Wong <slo.ryanwong@gmail.com>
Date:   Sun Jun 10 18:30:38 2018 -0500

    Creating a script to parallelize distribution of work across the SU network for HPC lab, exiting bug: Need to fix the simulator to accept the files from a different folder

commit e85c8d6a85724eb4e8185ff7a751df08221381dd
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Fri Jun 8 23:46:12 2018 -0400

    removing duplicate .zip file

commit 08c0e568fbb5fb726077933cd7d8eedaacf49644
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Fri Jun 8 18:55:40 2018 -0400

    changing git ignore to ignore output texts

commit f16ae732f61b29c72e49b437b770d01eec354d51
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Fri Jun 8 18:55:01 2018 -0400

    Starting writing script for mpi distribution, however need ubuntu/linux distribution for testing

commit 0aaf17ecfdb7600a6b6d37c5cb12d31bfb2c8c5d
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Fri Jun 8 09:57:58 2018 -0400

    Added 200k config

commit 3fab2f9cb6968f3b0d5b83a0dab708691b861dbb
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Thu Jun 7 11:28:08 2018 -0400

    added classification based on 0-15 topology

commit c9d47da312b749236ebc3cfab1fdf7d29d2f93d5
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Thu Jun 7 11:21:17 2018 -0400

    Added support to write to outfile that can be be used to train neural net - format : config, time

commit bea037928b30d915e7d43637bc22021c10ca3fd3
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Thu Jun 7 09:10:24 2018 -0400

    update gitignore to ignore *.pyc and *.out

commit 7b78ab33ba1cdd235e0afb76356af9f213bb55eb
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Thu Jun 7 09:09:24 2018 -0400

    adding command line argument support, renamed benchmark folder to remove space, added cwd to get path dynamically, wrote code to generate random configurations, beginning the threading process

commit ee13d5586fac6c0277866f763c70216ee88b6a09
Author: RyanWong5 <slo.ryanwong@gmail.com>
Date:   Tue Jun 5 10:24:17 2018 -0400

    REU Upload
