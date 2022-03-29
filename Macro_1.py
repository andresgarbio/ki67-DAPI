folder_name = "C:/Users/52871/Documents/CMU/Ambrosios Lab/Image analysis/Image analysis/Ki-67_03232022/"
treatments = range(0,2)
treatments_folder = ["fEV_ki67", "nEV_ki67"]
treatments_file = ["fEVs_ki67", "nEVs_ki67"]
samples = range(1,4)
channels = ["C1", "C2"]
image_numbers = range(1,11)
for treatment in treatments:
    for sample in samples:
        for image_number in image_numbers:
            folder_name = "C:/Users/52871/Documents/CMU/Ambrosios Lab/Image analysis/Image analysis/Ki-67_03232022/"
            for treatment in treatments:
                for sample in samples:
                    for image_number in image_numbers:
                        if(treatment == 0 and sample == 1 and image_number == 6):
                            continue
                        imp1 = IJ.openImage(folder_name + treatments_folder[treatment] + "/" + "C1" + "-" + str(sample) + "_" + treatments_file[treatment] +" red_" + str(image_number) + ".tif");
                    	IJ.run(imp1, "Color Threshold...", "");
                    	IJ.run(imp1, "16-bit", "");
                    	imp2 =  IJ.openImage(folder_name + treatments_folder[treatment] + "/"  + "C2" + "-" + str(sample) + "_" + treatments_file[treatment] +" red_" + str(image_number) + ".tif");
                    	IJ.run(imp2, "Color Threshold...", "");
                    	IJ.run(imp2, "16-bit", "");
                    	imp3 = ImageCalculator.run(imp1, imp2, "AND create");
                    	imp3.show();
                    	IJ.setAutoThreshold(imp1, "Default dark");
                    	IJ.run(imp1, "Convert to Mask", "");
                    	IJ.run(imp1, "Analyze Particles...", "size=40-Infinity pixel show=Overlay display include summarize overlay");
                    	IJ.setAutoThreshold(imp3, "Default dark");
                    	IJ.run(imp3, "Convert to Mask", "");
                    	IJ.run(imp3, "Analyze Particles...", "size=40-Infinity pixel show=Overlay display include summarize overlay");
                    	IJ.saveAs("Results", "C:/Users/52871/Documents/CMU/Ambrosios Lab/Image analysis/Image analysis/Ki-67_03232022/Results/test_results_" + str(treatment) + "_" + str(sample) + "_" + str(image_number) + ".csv");
                    	IJ.run("Close");
                    	IJ.run("Close");