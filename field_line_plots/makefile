TIMESTEPS=$(shell echo {00..50})
MONTAGE_OUTPUT=$(addsuffix .png,$(addprefix montage/,$(TIMESTEPS)))

RAW_IMAGES=$(shell ls raw/*.png)
OUTPUT_IMAGES=$(addprefix cropped/,$(notdir $(RAW_IMAGES:%.png=%_cropped.png)))

all: raw

.PHONY: raw
raw:
	mkdir -p raw
	cd ./raw;\
	rm -f $(shell find . -size 0);\
	bash ../fill_filelist.sh;\
	visit -nowin -cli -s ../plot.py

.PHONY: cropped
cropped:
	mkdir -p cropped
	$(MAKE) -C . $(OUTPUT_IMAGES)

cropped/%_cropped.png: raw/%.png
	convert $< -trim $@

.PHONY: clean
clean:
	rm -f raw/*.png raw/visitlog.py raw/filename_list
