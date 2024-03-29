import java.io.IOException;
import java.util.StringTokenizer;
import java.util.concurrent.TimeUnit;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CharCount {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      
      StringTokenizer itr = new StringTokenizer(value.toString());
      
      while (itr.hasMoreTokens()) {
        String str = itr.nextToken();

        if(str.length() == 6){
          word.set("6");
          context.write(word, one);

        }
        else if(str.length() == 8){
          word.set("8");
          context.write(word, one);
        }
      }
    }
  }

  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {

        sum += val.get();
      }
      
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    long startTime = System.nanoTime();
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "char count");
    job.setJarByClass(CharCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    if(job.waitForCompletion(true) ){
      long stopTime = System.nanoTime();
      System.out.println("-------------------------- TEMPO --------------------------");
      double elapsedTimeInSecond = (double) (stopTime - startTime) / 1_000_000_000;
      System.out.println(elapsedTimeInSecond + " segundos");
      long convert = TimeUnit.SECONDS.convert((stopTime - startTime), TimeUnit.NANOSECONDS);

      System.out.println(convert + " segundos");
      System.exit(0);
    } 
  }
}