# Cloud Technical Questions

### How do you shutdown a web site or service if you have no

1. Point the DNS records to a different serve

   - A (Address Mapping Records) : IPv4 주소 ex. 192.0.02.1
   - AAAA (IP Version 6 Address Records) : IPv6 주소를 알려준다.
   - CNAME (Canonical Name): 도메인 이름의 별칭을 만듬. A레코드로 대체시 성능 오버헤드를 줄임
     예제.. www.test.com -> test.com 의 다른 도메인명
   - The problem of this solution is that when you update DNS records, it will take a lot of time. 
     This is called DNS propagation and the time it takes depends on DNS servers. 
     (1 day ~ 1 month)

2. Change public IP addresses used for virtual machine. 

   - In GCP, you can change **external static IP** address in VPN menu. 
   - In AWS, you can change public IP address in Elastic IP menu

3. If the server is right next to me, then I can press the restart button. 
   In GRUB mode, select a recovery mode, and go to the command window. 

   ```
   mount -o remount,rw /
   passwd root
   ```

   The above command will reset the user's password. 

4. Pull the plug




# Bigdata Solution

## Hadoop

### Pros

1. **Open Source**
2. **Distributed processing** : Data is storated in a distributed manner in HDFS across the cluster. Data is processed in parallel. 
3. **Data is High available** and accessible. Since data is copied in multiple nodes, data is accessible from another data nodes even if a machine or hardware crashes. 
4. **Fault tolerant**: 3 replicas of each block is stored across the cluster, So if any node goes down, data can be recovered from the other node easily. 
5. Cheap commodity hardware. 

### cons

1. Not suitable for small data. HDFS is not efficient for random reading of small files because of its high capacity design. 
   (Small files are smaller than the HDFS block size (64MB or 128MB) and NameNode will be overloaded since it stores the namespace of HDFs)

1. - Solution

   - - Merge the small files to bigger file. 
     - HAR Files (Hadoop Archives): It solves name nodes' memory issue. but it is also not efficient for accessing small files in HDFS because HAR file access requires two index files read as well as the data file to read. it is slower
     - **Sequnce files**: It solve small file problem. We use filename as the key and the file contents as the value. And we can put them into a single sequence file. 
     - **HBase :** Hbase is common design pattern but you need to understand the hbase query and maintenance is not easy. 

2. Not Real-time data processing. : Hadoop is designed for **batch processing**. Although Batch processing is very efficient for processing a high volume of data, but depending on the size of the data, output can be delayed significantly. 

   - Solution
     - **Apache Spark**: Apache spark support streaming processing. 
     - **Apache Flink**: provides single run-time for the streaming as well as batch processing.

3. Security. Hadoop does not support encryption. 
   In Authentication, You can use Kerberos which is hard to manage. 



## BigQuery

BigQuery is an SQL-based Data Warehouse as a Service (DWaaS) that requires no upfront hardware provisioning or management. 

Single queries can cover petabyte-sized datasets and utilise thousands of CPUs distributed across hundreds of machines. While you aren't running queries, you only pay a tiny amount for data stored (0.02 per GB  per month)

### Pros

1. Zero ongoing operational overhead. (Infinite storage, thousands of CPU cores, massive network bandwidth, and virtually zero operational overhead.) 
2. Bulk Upload: CSV, JSON-per-oline file formats are supported. If your data is in S3, with Embulk you can easily move data in S3 to BigQuery. 
3. Streaming Upload. It supports lots of languages including Python. All you have to do is to use API. 
   (But you need to pay attention to the cost)



## Redshift

### Pros

1. Copy form S3: You can load data into Redsihft via COPY command. 
   Or you can use Embulk. 

### Cons

1. Redshift will ask you to choose a number of CPUs, RAM, HD, etc, to turn tem on. 
   While BigQuery doesn't care. No provisioning required
2. Even when you are running nothing, Redshift ask you to pay per hour of each of servers running. 
   While BigQuery only charges you $0.02 per month per GB stored. 
3. Redshift performance is limited by the amount of CPUs you are paying for.
   While BigQuery transparently brings in as many resources as needed to run your query in seconds. 
4. Redshift will ask you to index (distribute) your data. You will only be able to run fast queries based on this setting.
   While BigQuery has no indexes and every operation is simply fast. 
5. Streaming is in practice impossible. 
   While BigQuery supports ingesting up to 100, 000 rows per seconds per table 
6. Concurrent connections is painful with RedShift. 
   While BigQuery will just work. 



## MongoDB

### Pros

1. Schema-less. If you have a flexible schema. Simply saying, it is JSON format and you just put json data on MongoDB without schema. 
2. Easy scale out. MongoDB supports auto balancing, meaning you just add another machine on the cluster it will distribute your data balanced automatically. 

### Cons

1. No transaction. But atomic operations are supported at a single document level. 
2. Map Reduce (aggregations) is OK, but not that fast. I'd recommend Hadoop. 



## Elasticsearch

### Pros

1. Built on top of Lucene. It offers most powerful full-text search capabilities. 
2. ELK (Elasticsearch, Logstash, Kibana)
   - Elasticsearch is distributed, real-time search and analytics engine. 
   - Logstash is for parsing your log data and streaming it into Elasticsearch. 
   - Kibana is nice UI layer that gives you the ability to search and graph your data. 
3. Support Restful API
4. Actually free. But if you have security issue or machine learning features you need to subscribe paid version. 
5. Highly scalable. Clustering, replication of data, automatic failover is supported. 
   In most cases, you can run expensive queries in real time, which are typically run as batch processing in Hadoop. 

### Cons

1. Eventual consistency. The data you index is only available for search after 1 sec. 
   This process is known as **refresh wakes up** every 1 sec by default and makes the data searchable. 
2. Does not support SQL like joins. 
3. Does not support transactions and rollbacks. Transactions in a distributed system are expensive. 
4. Updates are expensive. An update on the existing document deletes the document and re-inserts it as a new document. 
5. Elasticsearch might lose data (Network partitions)
6. Multiple nodes going down at the same time. 



## Apache Hive

### Pros

1. It supports SQL-Like language called HiveQL (HQL)
2. Multiple users can simultaneous query for the data using HiveQL
3. It can deal with large data (1PB of data)
4. string functions are available

### Cons

1. Hive supports over-writing and appending data but not updates and deletes 
2. Sub-queries are not supported



## Apache Ignite 

### Pros

1. In-memory big data solution. It is super fast.
2. It solves small file problem in HDFS and Spark. 
   SUPER FAST





