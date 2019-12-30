from pds_pipelines.config import pds_log, slurm_log, cmd_dir

log_format = '%(asctime)s - %(name)s - %(levelname)s, %(message)s'

jobconfig = {'di': {'logger': 'di_process_hpc_job',
                    'handle': pds_log + 'DI.log',
                    'info': 'Starting DI Process HPC Job Submission',
                    'name': 'pds_di_process',
                    'stdout': slurm_log + 'di_process_%A_%a.out',
                    'stderr': slurm_log + 'di_process_%A_%a.err',
                    'memory': '256',
                    'wallclock': '240:00:00',
                    'partition': 'pds',
                    'cmd': cmd_dir + 'di_process.py',
                    'SBfile': slurm_log + 'DIhpc@date@.sbatch'},
             'upc': {'logger': 'upc_process_hpc_job',
                    'handle': pds_log + 'UPC.log',
                    'info': 'Starting UPC Process HPC Job Submission',
                    'name': 'pds_upc_process',
                    'stdout': slurm_log + 'upc_process_%A_%a.out',
                    'stderr': slurm_log + 'upc_process_%A_%a.err',
                    'memory': '8192',
                    'wallclock': '20:00:00',
                    'partition': 'pds',
                    'cmd': cmd_dir + 'upc_process.py',
                    'SBfile': slurm_log + 'upc_hpc@date@.sbatch'},
             'ingest': {'logger': 'ingest_process_hpc_job',
                        'handle': pds_log + 'Ingest.log',
                        'info': 'Starting Ingest Process HPC Job Submission',
                        'name': 'pds_ingest_process',
                        'stdout': slurm_log + 'ingest_process_%A_%a.out',
                        'stderr': slurm_log + 'ingest_process_%A_%a.err',
                        'memory': '8192',
                        'wallclock': '240:00:00',
                        'partition': 'pds',
                        'cmd': cmd_dir + 'ingest_process.py',
                        'SBfile': slurm_log + 'Ingesthpc@date@.sbatch'},
             'thumbnail': {'logger': 'thumbnail_process_hpc_job',
                           'handle': pds_log + 'Process.log',
                            'info': 'Starting Thumbnail Process HPC Job Submission',
                            'name': 'pds_thumbnail_process',
                            'stdout': slurm_log + 'thumbnail_process_%A_%a.out',
                            'stderr': slurm_log + 'thumbnail_process_%A_%a.err',
                            'memory': '8192',
                            'wallclock': '20:00:00',
                            'partition': 'pds',
                            'cmd': cmd_dir + 'thumbnail_process.py',
                            'SBfile': slurm_log + 'Thpc@date@.sbatch'},
             'browse': {'logger': 'browse_process_hpc_job',
                        'handle': pds_log + 'Process.log',
                        'info': 'Starting Browse Process HPC Job Submission',
                        'name': 'PDS_Browseprocess',
                        'stdout': slurm_log + 'browse_process_%A_%a.out',
                        'stderr': slurm_log + 'browse_process_%A_%a.err',
                        'memory': '8192',
                        'wallclock': '20:00:00',
                        'partition': 'pds',
                        'cmd': cmd_dir + 'browse_process.py',
                        'SBfile': slurm_log + 'Bhpc@date@.sbatch'}
             }
