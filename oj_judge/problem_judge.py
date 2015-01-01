#!/usr/bin/python
import shlex,subprocess,os,time
import filecmp
import shutil
import random

def run(sid,pid,source,lang,timelimit,memlimit):
	judge_result={
		'result': 'CE',
		'status': 0,
		'time': 0,
		'memory': 0,
		'message': ''
		}

	run_dir='/home/ISeaTeL/ISeaTeL_Cup_Site/oj_judge/run/%d' % sid
	prob_dir='../../../media/problem/%d' % pid
	print run_dir, prob_dir
	
	shutil.rmtree(run_dir, ignore_errors=True)

	os.mkdir(run_dir)
	os.chdir(run_dir)
	
	print source

	cmd={}
	fname={}
	fname['GCC']='Main.c'
	fname['G++']='Main.cpp'
	f=file(fname[lang],'w')
	f.write(source)
	f.close()
	cmd['GCC']='gcc -static Main.c -o Main'
	cmd['G++']='g++ -static Main.cpp -o Main'
	cmd['JAVA']='javac Main.java'
	fd1=file('out','w')
	fd2=file('err','w')

	print cmd[lang]

	p=subprocess.Popen(shlex.split(cmd[lang]),stdout=fd1,stderr=fd2)
	p.wait()
	fd1.close()
	fd2.close()
	if p.returncode!=0:
		e=file('err','r')
		judge_result['message']=e.read()
		return judge_result
	cmd['GCC']='sudo ../antiskill -i %s/in -o out -t %d -m %d Main' % (prob_dir, timelimit, memlimit)
	cmd['G++']='sudo ../antiskill -i %s/in -o out -t %d -m %d Main' % (prob_dir, timelimit, memlimit)
	
	print cmd[lang]
	
	msg=file('msg','w')
	p=subprocess.Popen(shlex.split(cmd[lang]),stdout=msg)

	while True:
		if p.poll()!=None:
			msg.close()
			msg=file('msg','r')
			result=msg.read()
			msg.close()
			result=result.replace('\n', '').split(' ')
			result, status, time_usage, mem_usage = result
			
			judge_result={
					'result': result,
					'status': status,
					'time': time_usage,
					'memory': mem_usage,
				    'message': 'OK'
                }

			if(result == 'OK'):
				out='out'
				outdata='%s/out' % (prob_dir)
				if filecmp.cmp(out, outdata):
					judge_result['result'] = 'AC'
				else:
					judge_result['result'] = 'WA'
			elif(result == 'RE' or result == 'MLE' or result == 'TLE'):
				pass
			else:
				judge_result['result': 'JudgeError']

			return judge_result

if __name__=='__main__':
	ff=file('source.c','r')
	s=ff.read()
	lang='G++'
	timelimit=1000
	memlimit=32000
	sid=random.randint(10,1000)
	pid=1
	shutil.rmtree('./run/%d' % sid, ignore_errors=True)

	print run(sid,pid,s,lang,timelimit,memlimit)
	
