/* user and group to drop privileges to */
static const char *user  = "lominoss";
static const char *group = "users";

static const char *colorname[NUMCOLS] = {
	[INIT] =   "#2e3440",     /* after initialization */
	[INPUT] =  "#eceff4",   /* during input */
	[FAILED] = "#bf616a",   /* wrong password */
};

/* treat a cleared input like a wrong password (color) */
static const int failonclear = 1;
