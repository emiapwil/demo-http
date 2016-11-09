

democlient: curl_progress.o curl_progress.c
	gcc -o democlient -lcurl $<

clean:
	rm -rf democlient curl_progress.o
