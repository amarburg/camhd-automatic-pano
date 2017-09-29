require 'pathname'


photoscan_bin = "/opt/photoscan-pro/photoscan.sh"

task :default do
  sh photoscan_bin, "-r", "scripts/photoscan.py"   #, "--input", "images/CAMHDA301-20170915T001500/"
end

task :help do
  sh photoscan_bin, "--help"
end



pano_files = ['../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T001500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T031500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T061500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T091500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T121500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T151500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T181500_optical_flow_regions.json',
              '../CamHD_motion_metadata/RS03ASHS/PN03B/06-CAMHDA301/2017/09/15/CAMHDA301-20170915T211500_optical_flow_regions.json']

namespace :pano do

  task :extract do

    pano_files.each { |p|
      sh "python", "scripts/extract_images.py",
          "--lazycache-url", "http://ursine:8080/v1/org/oceanobservatories/rawdata/files/",
          "--mov-output-dir", p
    }

  end

  task :photoscan do

    pano_files.first(2).each { |p|

      base = Pathname.new(p).basename
      base = base.sub(/_optical_flow_regions.json/, "")


      input_file = "images/%s" % base
      project_file = "projects/%s.psx" % base

      sh photoscan_bin, "-r", "scripts/photoscan.py", "--input", input_file, "--save-project-as", project_file

    }
  end

end
