/*
 * Initially allocated size of a ResourceArray.  Must be power of two since
 * we'll use (arraysize - 1) as mask for hashing.
 */
#define RESARRAY_INIT_SIZE 16

/*
 * When to switch to hashing vs. simple array logic in a ResourceArray.
 */
#define RESARRAY_MAX_ARRAY 64

/* Minimum amount to read at a time */
#define MIN_READ_SIZE 4096

#define PGSTAT_ENTRY_REF_HASH_SIZE	128

/* ----------
 * Initial size hints for the hash tables used in statistics.
 * ----------
 */

#define PGSTAT_SNAPSHOT_HASH_SIZE	512

/*
 * The size of the initial DSM segment that backs a dsa_area created by
 * dsa_create.  After creating some number of segments of this size we'll
 * double this size, and so on.  Larger segments may be created if necessary
 * to satisfy large requests.
 */
#define DSA_INITIAL_SEGMENT_SIZE ((size_t) (1 * 1024 * 1024))

/*
 * How many segments to create before we double the segment size.  If this is
 * low, then there is likely to be a lot of wasted space in the largest
 * segment.  If it is high, then we risk running out of segment slots (see
 * dsm.c's limits on total number of segments), or limiting the total size
 * an area can manage when using small pointers.
 */
#define DSA_NUM_SEGMENTS_AT_EACH_SIZE 2

/*
 * Initial size of memtuples array.  We're trying to select this size so that
 * array doesn't exceed ALLOCSET_SEPARATE_THRESHOLD and so that the overhead of
 * allocation might possibly be lowered.  However, we don't consider array sizes
 * less than 1024.
 *
 */
#define INITIAL_MEMTUPSIZE Max(1024, \
	ALLOCSET_SEPARATE_THRESHOLD / sizeof(SortTuple) + 1)


/*
 * During merge, we use a pre-allocated set of fixed-size slots to hold
 * tuples.  To avoid palloc/pfree overhead.
 *
 * Merge doesn't require a lot of memory, so we can afford to waste some,
 * by using gratuitously-sized slots.  If a tuple is larger than 1 kB, the
 * palloc() overhead is not significant anymore.
 *
 * 'nextfree' is valid when this chunk is in the free list.  When in use, the
 * slot holds a tuple.
 */
#define SLAB_SLOT_SIZE 1024


/*
 * Parameters for calculation of number of tapes to use --- see inittapes()
 * and tuplesort_merge_order().
 *
 * In this calculation we assume that each tape will cost us about 1 blocks
 * worth of buffer space.  This ignores the overhead of all the other data
 * structures needed for each tape, but it's probably close enough.
 *
 * MERGE_BUFFER_SIZE is how much buffer space we'd like to allocate for each
 * input tape, for pre-reading (see discussion at top of file).  This is *in
 * addition to* the 1 block already included in TAPE_BUFFER_OVERHEAD.
 */
#define MINORDER		6		/* minimum merge order */
#define MAXORDER		500		/* maximum merge order */
#define TAPE_BUFFER_OVERHEAD		BLCKSZ
#define MERGE_BUFFER_SIZE			(BLCKSZ * 32)


/*
 * Constants
 *
 * A hash table has a top-level "directory", each of whose entries points
 * to a "segment" of ssize bucket headers.  The maximum number of hash
 * buckets is thus dsize * ssize (but dsize may be expansible).  Of course,
 * the number of records in the table can be larger, but we don't want a
 * whole lot of records per bucket or performance goes down.
 *
 * In a hash table allocated in shared memory, the directory cannot be
 * expanded because it must stay at a fixed address.  The directory size
 * should be selected using hash_select_dirsize (and you'd better have
 * a good idea of the maximum number of entries!).  For non-shared hash
 * tables, the initial directory size can be left at the default.
 */
#define DEF_SEGSIZE			   256
#define DEF_SEGSIZE_SHIFT	   8	/* must be log2(DEF_SEGSIZE) */
#define DEF_DIRSIZE			   256

/* Number of freelists to be used for a partitioned hash table. */
#define NUM_FREELISTS			32


/*
 * The size of chunks, in pages.  This is somewhat arbitrarily set to match
 * the size of HASH_CHUNK, so that Parallel Hash obtains new chunks of tuples
 * at approximately the same rate as it allocates new chunks of memory to
 * insert them into.
 */
#define STS_CHUNK_PAGES 4

/*
 * Control how many partitions are created when spilling HashAgg to
 * disk.
 *
 * HASHAGG_PARTITION_FACTOR is multiplied by the estimated number of
 * partitions needed such that each partition will fit in memory. The factor
 * is set higher than one because there's not a high cost to having a few too
 * many partitions, and it makes it less likely that a partition will need to
 * be spilled recursively. Another benefit of having more, smaller partitions
 * is that small hash tables may perform better than large ones due to memory
 * caching effects.
 *
 * We also specify a min and max number of partitions per spill. Too few might
 * mean a lot of wasted I/O from repeated spilling of the same tuples. Too
 * many will result in lots of memory wasted buffering the spill files (which
 * could instead be spent on a larger hash table).
 */
#define HASHAGG_PARTITION_FACTOR 1.50
#define HASHAGG_MIN_PARTITIONS 4
#define HASHAGG_MAX_PARTITIONS 1024

/*
 * For reading from tapes, the buffer size must be a multiple of
 * BLCKSZ. Larger values help when reading from multiple tapes concurrently,
 * but that doesn't happen in HashAgg, so we simply use BLCKSZ. Writing to a
 * tape always uses a buffer of size BLCKSZ.
 */
#define HASHAGG_READ_BUFFER_SIZE BLCKSZ
#define HASHAGG_WRITE_BUFFER_SIZE BLCKSZ

/*
 * HyperLogLog is used for estimating the cardinality of the spilled tuples in
 * a given partition. 5 bits corresponds to a size of about 32 bytes and a
 * worst-case error of around 18%. That's effective enough to choose a
 * reasonable number of partitions when recursing.
 */
#define HASHAGG_HLL_BIT_WIDTH 5

/*
 * Estimate chunk overhead as a constant 16 bytes. XXX: should this be
 * improved?
 */
#define CHUNKHDRSZ 16


/*
 * Sorting many small groups with tuplesort is inefficient. In order to
 * cope with this problem we don't start a new group until the current one
 * contains at least DEFAULT_MIN_GROUP_SIZE tuples (unfortunately this also
 * means we can't assume small groups of tuples all have the same prefix keys.)
 * When we have a bound that's less than DEFAULT_MIN_GROUP_SIZE we start looking
 * for the new group as soon as we've met our bound to avoid fetching more
 * tuples than we absolutely have to fetch.
 */
#define DEFAULT_MIN_GROUP_SIZE 32

/*
 * Default size; large enough that typical users of XLogReader won't often need
 * to use the 'oversized' memory allocation code path.
 */
#define DEFAULT_DECODE_BUFFER_SIZE (64 * 1024)

/*
 * When maintenance_io_concurrency is not saturated, we're prepared to look
 * ahead up to N times that number of block references.
 */
#define XLOGPREFETCHER_DISTANCE_MULTIPLIER 4

/*
 * Space/time tradeoff parameters: do these need to be user-tunable?
 *
 * To consider truncating the relation, we want there to be at least
 * REL_TRUNCATE_MINIMUM or (relsize / REL_TRUNCATE_FRACTION) (whichever
 * is less) potentially-freeable pages.
 */
#define REL_TRUNCATE_MINIMUM	1000
#define REL_TRUNCATE_FRACTION	16

/*
 * Timing parameters for truncate locking heuristics.
 *
 * These were not exposed as user tunable GUC values because it didn't seem
 * that the potential for improvement was great enough to merit the cost of
 * supporting them.
 */
#define VACUUM_TRUNCATE_LOCK_CHECK_INTERVAL		20	/* ms */
#define VACUUM_TRUNCATE_LOCK_WAIT_INTERVAL		50	/* ms */
#define VACUUM_TRUNCATE_LOCK_TIMEOUT			5000	/* ms */

/*
 * Threshold that controls whether we bypass index vacuuming and heap
 * vacuuming as an optimization
 */
#define BYPASS_THRESHOLD_PAGES	0.02	/* i.e. 2% of rel_pages */

/*
 * Perform a failsafe check each time we scan another 4GB of pages.
 * (Note that this is deliberately kept to a power-of-two, usually 2^19.)
 */
#define FAILSAFE_EVERY_PAGES \
	((BlockNumber) (((uint64) 4 * 1024 * 1024 * 1024) / BLCKSZ))

/*
 * When a table has no indexes, vacuum the FSM after every 8GB, approximately
 * (it won't be exact because we only vacuum FSM after processing a heap page
 * that has some removable tuples).  When there are indexes, this is ignored,
 * and we vacuum FSM after each index/heap cleaning pass.
 */
#define VACUUM_FSM_EVERY_PAGES \
	((BlockNumber) (((uint64) 8 * 1024 * 1024 * 1024) / BLCKSZ))

/*
 * Before we consider skipping a page that's marked as clean in
 * visibility map, we must've seen at least this many clean pages.
 */
#define SKIP_PAGES_THRESHOLD	((BlockNumber) 32)

/*
 * Size of the prefetch window for lazy vacuum backwards truncation scan.
 * Needs to be a power of 2.
 */
#define PREFETCH_SIZE			((BlockNumber) 32)

/*
 * Size of the LRU list.
 *
 * Note: the code assumes that SYNC_SCAN_NELEM > 1.
 *
 * XXX: What's a good value? It should be large enough to hold the
 * maximum number of large tables scanned simultaneously.  But a larger value
 * means more traversing of the LRU list when starting a new scan.
 */
#define SYNC_SCAN_NELEM 20

#define MQH_INITIAL_BUFSIZE				8192

/* RELSEG_SIZE is the maximum number of blocks allowed in one disk file. Thus,
   the maximum size of a single file is RELSEG_SIZE * BLCKSZ; relations bigger
   than that are divided into multiple files. RELSEG_SIZE * BLCKSZ must be
   less than your OS' limit on file size. This is often 2 GB or 4GB in a
   32-bit operating system, unless you have large file support enabled. By
   default, we make the limit 1 GB to avoid any possible integer-overflow
   problems within the OS. A limit smaller than necessary only means we divide
   a large relation into more chunks than necessary, so it seems best to err
   in the direction of a small limit. A power-of-2 value is recommended to
   save a few cycles in md.c, but is not absolutely required. Changing
   RELSEG_SIZE requires an initdb. */
#define RELSEG_SIZE 131072


/*
 * PostgreSQL normally uses 8kB pages for most things, but many common
 * architecture/operating system pairings use a 4kB page size for memory
 * allocation, so we do that here also.
 */
#define FPM_PAGE_SIZE			4096

/*
 * Maximum length for identifiers (e.g. table names, column names,
 * function names).  Names actually are limited to one fewer byte than this,
 * because the length must include a trailing zero byte.
 *
 * Changing this requires an initdb.
 */
#define NAMEDATALEN 64

/*
 * When we don't have native spinlocks, we use semaphores to simulate them.
 * Decreasing this value reduces consumption of OS resources; increasing it
 * may improve performance, but supplying a real spinlock implementation is
 * probably far better.
 */
#define NUM_SPINLOCK_SEMAPHORES		128


/*
 * Preferred alignment for disk I/O buffers.  On some CPUs, copies between
 * user space and kernel space are significantly faster if the user buffer
 * is aligned on a larger-than-MAXALIGN boundary.  Ideally this should be
 * a platform-dependent value, but for now we just hard-wire it.
 */
#define ALIGNOF_BUFFER	32

/*
 * Assumed cache line size. This doesn't affect correctness, but can be used
 * for low-level optimizations. Currently, this is used to pad some data
 * structures in xlog.c, to ensure that highly-contended fields are on
 * different cache lines. Too small a value can hurt performance due to false
 * sharing, while the only downside of too large a value is a few bytes of
 * wasted memory. The default is 128, which should be large enough for all
 * supported platforms.
 */
#define PG_CACHE_LINE_SIZE		128

/*
 * Assumed alignment requirement for direct I/O.  4K corresponds to common
 * sector and memory page size.
 */
#define PG_IO_ALIGN_SIZE		4096

/* Size of a disk block --- this also limits the size of a tuple. You can set
   it bigger if you need bigger tuples (although TOAST should reduce the need
   to have large tuples, since fields can be spread across multiple tuples).
   BLCKSZ must be a power of 2. The maximum possible value of BLCKSZ is
   currently 2^15 (32768). This is determined by the 15-bit widths of the
   lp_off and lp_len fields in ItemIdData (see include/storage/itemid.h).
   Changing BLCKSZ requires an initdb. */
#define BLCKSZ 8192


/* Size of a WAL file block. This need have no particular relation to BLCKSZ.
   XLOG_BLCKSZ must be a power of 2, and if your system supports O_DIRECT I/O,
   XLOG_BLCKSZ must be a multiple of the alignment requirement for direct-I/O
   buffers, else direct I/O may fail. Changing XLOG_BLCKSZ requires an initdb.
   */
#define XLOG_BLCKSZ 8192


/* TODO: Unscientifically determined threshold */
LLVMPassManagerBuilderUseInlinerWithThreshold(llvm_pmb, 512);


/* choose the maxBlockSize to be no larger than 1/16 of work_mem */
while (16 * maxBlockSize > work_mem * 1024L)
	maxBlockSize >>= 1;

