export LD_PRELOAD=${MKLROOT}/lib/intel64/libmkl_def.so
export LD_PRELOAD=${MKLROOT}/lib/intel64/libmkl_avx2.so:${LD_PRELOAD}
export LD_PRELOAD=${MKLROOT}/lib/intel64/libmkl_core.so:${LD_PRELOAD}
export LD_PRELOAD=${MKLROOT}/lib/intel64/libmkl_intel_lp64.so:${LD_PRELOAD}
export LD_PRELOAD=${MKLROOT}/lib/intel64/libmkl_intel_thread.so:
export LD_PRELOAD=${MKLROOT}../lib/intel64_lin/libiomp5.so
