# SAX
An up-to-date Python implementation of SAX

# PREPARATION

## PAPER

### Classical SAX
- Zan, Chaw Thet, and Hayato Yamana. "An improved symbolic aggregate approximation distance measure based on its statistical features." Proceedings of the 18th International Conference on Information Integration and Web-based Applications and Services. ACM, 2016.
- Sun, Youqiang, et al. "An improvement of symbolic aggregate approximation distance measure for time series." Neurocomputing 138 (2014): 189-198.
- Al-Hmouz, Rami, and Witold Pedrycz. "Models of time series with time granulation." Knowledge and Information Systems 48.3 (2016): 561-580.

### iSAX
- http://www.cs.ucr.edu/~eamonn/iSAX/iSAX.html. iSAX, a generalization of SAX that allows indexing and mining of massive datasets. 
- Camerra, Alessandro, et al. "iSAX 2.0: Indexing and mining one billion time series." Data Mining (ICDM), 2010 IEEE 10th International Conference on. IEEE, 2010.
- Shieh, Jin, and Eamonn Keogh. "i SAX: indexing and mining terabyte sized time series." Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2008.

### Features (Optional)
- Fotso, Vanel Steve Siyou, Engelbert Mephu Nguifo, and Philippe Vaslin. "Parameter Free Piecewise Dynamic Time Warping for time series classification." (2016).
- Castro, Nuno C., and Paulo J. Azevedo. "Automatically estimating iSAX parameters." Intelligent Data Analysis 19.3 (2015): 581-595.

## CODE

### Code review
 - https://github.com/dolaameng/pysax. 2 years ago.
 - https://github.com/nphoff/saxpy. 4 years ago.
 - https://github.com/melsabagh/sax. 3 years ago. In C++, but might be useful in the aspect of architecture.

## LEARNING RESOURCES

- Fournier-viger, Philippe. "Introduction to time series mining with SPMF - The Data Mining Blog." The Data Mining Blog. 18 Dec. 2016. Web. 7 Sept. 2017. <http://data-mining.philippe-fournier-viger.com/introduction-time-series-mining-spmf/>
- N.a. "Welcome to the iSAX page" Cs.ucr.edu. 26 May 2008. Web. 7 Sept. 2017. <http://www.cs.ucr.edu/~eamonn/iSAX/iSAX.html>
- N.a. "MLconf 2015 Seattle: How does the symbolic aggregate approximation (SAX) technique work? - Quora." Quora.com. n.d. Web. 7 Sept. 2017. <https://www.quora.com/MLconf-2015-Seattle/MLconf-2015-Seattle-How-does-the-symbolic-aggregate-approximation-SAX-technique-work>

# MILESTONE

## MINIMAL

- Simple SAX implementation. It works, that's all.
- Meet the requirement: robust, scalable.

## EXPECTED

From the latest paper, there are some features may be included in this implementation.

- GUI interface.
- Performance for a single time execution.
- Performance when tuning parameters.
- Automatically estimate parameters.
- Parameter free.

# PLAN

- Sep. 07 - Sep. 08. Figure out the SAX algorithm and related theories.
- Sep. 08 - Sep. 13. Meet the MINIMAL milestone. If there is spare time, add some features in the EXPECTED milestone.
- Sep. 14 - Sep. 14. Optimize the implementation.
- Sep. 15 - Sep. 15. Test.