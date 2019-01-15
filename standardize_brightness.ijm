function brightness(folder, output, filename) {
//run("Brightness/Contrast...");
open(folder + filename);
setMinAndMax(0, 2500);
run("Apply LUT");
run("Fire");
run("Apply LUT", "stack");
run("Calibration Bar...", "location=[Lower Right] fill=None label=White number=5 decimal=0 font=12 zoom=1 overlay");
saveAs("PNG", output + filename);
};
folder = "/Users/max/Desktop/Office/Phd/Data/N1E_115/SiRNA/SiRNA_26/100x_epo/";
output = folder + "zadjusted/";
setBatchMode(true);
list = getFileList(folder)
for (i = 0; i <list.length; i++){ 
if(endsWith(list[i],".TIF")&&indexOf(list[i],"mCherry")>=1){ 
		brightness(folder, output, list[i]);
}
}
setBatchMode(false);




