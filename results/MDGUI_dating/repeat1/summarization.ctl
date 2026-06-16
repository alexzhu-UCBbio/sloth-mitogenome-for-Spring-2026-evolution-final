          seed = -1
       seqfile = Delsuc-CurrBiol-2019_dataset.PML
      treefile = calibration_tree.nwk
      mcmcfile = all_mcmc_runs.txt
       outfile = summarization.out.txt
       
         ndata = 1 *
       seqtype = 0 *
       usedata = 2 out.BV *
         clock = 3 *
         model = 7 *
         alpha = 0.5 *
         ncatG = 4 *
     cleandata = 0 *
   kappa_gamma = 6.0 2.0 *
   alpha_gamma = 1.0 1.0 *

       BDparas = 1.0 1.0 0.0 c*
   
   rgene_gamma = 2.0 20.0 1.0 *
  sigma2_gamma = 1.0 10.0 1.0 *
  
         print = -1 *
        burnin = 0 *
      sampfreq = 100 *
       nsample = 50000 *
    checkpoint = 1 0.002 mcmctree.ckpt *
