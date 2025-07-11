hostnames = [
	['---------- V+ Internals ----------', '-----', '--', '----', '---------'],
	['mylist', '10.10.20.70', '22', 'kris', 'Usage: V+ MyList and LastWatch'],
	['re-engine', '10.10.20.50', '22', 'kris', 'Usage: V+ Recommendation Engine Service'],
	['re-engine-db', '10.10.20.5', '22', 'kris', 'Usage: V+ Recommendation Engine Service DB'],
	['re-engine-redis', '10.10.20.52', '22', 'kris', 'Usage: V+ Recommendation Engine Service: Redis'],
	['re-engine-stag', '10.10.19.167', '22', 'kris', 'Usage: V+ Recommendation Engine Service - Staging'],
	['content-tools-cms-lb', '10.10.20.122', '45817', 'kris', 'Usage: Content Tools CMS Production Load Balancer'],
	['content-tools-cms', '10.10.20.170', '22', 'kris', 'Usage: Content Tools CMS Production'],
	['content-tools-cms-stag', '10.10.19.102', '22', 'root', 'Usage: Content Tools CMS Staging'],
	['media-center', '10.10.19.172', '22', 'kris', 'Usage: Media Center Vision+'],
	['sms-node1', '10.10.19.131', '22', 'mncnow', 'Usage: SMS Service'],
	['special-tunnel', '10.10.19.200', '22', 'ksetyadi', 'Usage: Special Tunnel to Office'],
	['all-stags', '10.10.19.224', '22', 'mncnow', 'Usage: Voucher HUT + Ref ID Generator + Vmail + SMS'],
	['voucher-hut-prod', '10.10.19.135', '45817', 'kris', 'Usage: Voucher HUT Production'],
	['ref-gen-id', '10.10.19.133', '22', 'kris', 'Usage: Voucher KVision'],
	['vplus-meet-sgp1', '128.199.239.40', '22', 'root', 'Usage: Vplus Meet'],
	['test-lb', '128.199.228.97', '22', 'root', 'Usage: Test LB'],
	['test-xiaomi', '128.199.242.16', '22', 'root', 'Usage: Test Xiaomi'],
	['verify-email', '10.10.19.134', '22', 'kris', 'Usage: Verify Email MNC Group'],
	['vmail-prod', '10.10.19.132', '22', 'mncnow', 'Usage: Microservice Email Production'],
	['dl2go-prod', '10.10.20.39', '22', 'kris', 'Usage: Download To Go Production'],
	['db-explore', '10.10.19.70', '22', 'kris', 'Usage: Vision+ Data Exploration'],
	['app-rating', '10.10.20.171', '22', 'kris', 'Usage: Vision+ App Rating'],
	['atvlogin-lb1', '10.10.20.151', '45817', 'kris', 'Usage: ATV Login Load Balancer'],
	['atvlogin1', '10.10.21.48', '22', 'kris', 'Usage: ATV Login Server 3'],
	['atvlogin2', '10.10.21.49', '22', 'kris', 'Usage: ATV Login Server 4'],
	['atvlogin-redis', '10.10.21.46', '22', 'kris', 'Usage: ATV Login Redis'],
	['atvlogin-db', '10.10.20.46', '22', 'kris', 'Usage: ATV Login Database'],
	['vp-metabase', '209.97.171.247', '22', 'kris', 'Usage: Vision+ Metabase'],
	['inbox', '10.10.20.51', '22', 'kris', 'Usage: V+ Inbox'],
	['ptvgw-lb', '10.10.20.127', '45817', 'kris', 'Usage: V+ PayTV Gateway Load Balancer'],
	['ptvgw-prod', '10.10.20.65', '22', 'kris', 'Usage: V+ PayTV Gateway'],
	['ptvgw-redis', '10.10.20.100', '22', 'kris', 'Usage: V+ PayTV Gateway Redis'],
	['url_shortener', '10.10.20.171', '22', 'kris', 'Usage: V+ URL Shortener'],
	['vp-appconfig', '159.65.136.67', '22', 'root', 'Usage: V+ App Config'],
	['vp-versioning', '159.65.136.81', '22', 'root', 'Usage: V+ Versioning'],
	['vp-adtools', '10.10.20.21', '22', 'kris', 'Usage: V+ AdTools'],
	['database1-prod', '10.10.20.59', '45817', 'kris', 'Usage: V+ Database Production 1'],
	['lastwatch-api1', '10.10.20.67', '22', 'kris', 'Usage: V+ Last Watch API 1'],
	['lastwatch-api2', '10.10.20.68', '22', 'kris', 'Usage: V+ Last Watch API 2'],
	['lastwatch-redis', '10.10.20.66', '22', 'kris', 'Usage: V+ Database Production Redis Continue Watching'],	
	['mongodb-cont', '10.10.20.220', '22', 'kris', 'Usage: V+ Database Production MongoDB Continue Watching'],	
	['redis-db-staging', '10.10.19.144', '22', 'kris', 'Usage: V+ Redis DB Staging'],	 
	['---------- V+ PROXYSQL ----------', '-----', '--', '----', '---------'],
	['proxysql', '10.10.20.179', '45817', 'kris', 'Usage: V+ ProxySQL'],
	['---------- V+ PRODUCTION LB App ----------', '-----', '--', '----', '---------'],
	['lb-app-1', '10.10.20.154', '45817', 'kris', 'Usage: V+ LB'],
	['lb-app-2', '10.10.20.155', '45817', 'kris', 'Usage: V+ LB'],
	['---------- V+ PRODUCTION LB Web ----------', '-----', '--', '----', '---------'],
	['lb-web-1', '10.10.19.61', '45817', 'kris', 'Usage: V+ LB'],
	['lb-web-2', '10.10.19.62', '45817', 'kris', 'Usage: V+ LB'],
	['lb-web-3', '10.10.20.151', '45817', 'kris', 'Usage: V+ LB'],
	['lb-web-4', '10.10.20.152', '45817', 'kris', 'Usage: V+ LB'],
	['---------- V+ PRODUCTION APPS API ----------', '-----', '--', '----', '---------'],
	['app-api-1', '10.10.20.201', '22', 'kris', 'Usage: V+ APP'],
	['app-api-2', '10.10.20.202', '22', 'kris', 'Usage: V+ APP'],
	['app-api-3', '10.10.20.203', '22', 'kris', 'Usage: V+ APP'],
	['app-api-4', '10.10.20.204', '22', 'kris', 'Usage: V+ APP'],
	['app-api-5', '10.10.20.205', '22', 'kris', 'Usage: V+ APP'],
	['app-api-6', '10.10.20.206', '22', 'kris', 'Usage: V+ APP'],
	['app-api-7', '10.10.20.207', '22', 'kris', 'Usage: V+ APP'],
	['---------- V+ LB CONTENT ----------', '-----', '--', '----', '---------'],
	['lb-content-1', '10.10.20.120', '45817', 'kris', 'Usage: V+ CONTENT LB'],
	['lb-content-2', '10.10.20.121', '45817', 'kris', 'Usage: V+ CONTENT LB'],
	['lb-content-3', '10.10.20.122', '45817', 'kris', 'Usage: V+ CONTENT LB'], 
	['lb-content-4', '10.10.20.123', '45817', 'kris', 'Usage: V+ CONTENT LB'], 
	['---------- V+ PRODUCTION WEB API ----------', '-----', '--', '----', '---------'],
	['web-api-1', '10.10.20.211', '22', 'kris', 'Usage: V+ Web API'],
	['web-api-2', '10.10.20.212', '22', 'kris', 'Usage: V+ Web API'],
	['web-api-3', '10.10.20.213', '22', 'kris', 'Usage: V+ Web API'],
	['web-api-4', '10.10.20.214', '22', 'kris', 'Usage: V+ Web API'],
	['web-api-5', '10.10.20.215', '22', 'kris', 'Usage: V+ Web API'],
	['web-api-6', '10.10.20.216', '22', 'kris', 'Usage: V+ Web API'],
	['---------- V+ PRODUCTION WEB  ----------', '-----', '--', '----', '---------'],
	['nweb-1', '10.10.19.161', '45817', 'kris', 'Usage: V+ Web'],
	['nweb-2', '10.10.19.162', '45817', 'kris', 'Usage: V+ Web'],
	['nweb-3', '10.10.19.163', '45817', 'kris', 'Usage: V+ Web'],
	['nweb-4', '10.10.19.164', '45817', 'kris', 'Usage: V+ Web'],
	['nweb-5', '10.10.19.165', '45817', 'kris', 'Usage: V+ Web'],
	['---------- PLAYBOX ----------', '-----', '--', '----', '---------'],
	['playbox-web', '10.10.21.160', '22', 'kris', 'Usage: Playbox website'],
	['playbox-pgsql', '10.10.21.161', '22', 'kris', 'Usage: Playbox website postgres'],
	['---------- PERSONAL ----------', '-----', '--', '----', '---------'],
	['meowmagz', '206.189.208.77', '22', 'root', 'Usage: Meowmagz Server'],
	['orion-sgp1', '167.99.67.233', '22', 'root', 'Usage: Orion Server'],
	['ubuntu-api-gateway', '188.166.248.126', '22', 'root', 'Usage: API Gateway Server'],
	['---------- TUNAS RIDEAN ----------', '', '', '', ''],
	['tunas-epms-owned', '165.22.241.218', '22', 'root', 'Usage: Tunas E-PMS Owned'],
	['tunas-staging-owned', '139.59.110.101', '22', 'root', 'Usage: Tunas E-PMS Staging'],
	['---------- 7Spectrum ------------------------', '', '', '', ''],
	['7spc-prod', '206.189.95.24', '35789', 'root', 'Usage: 7 Spectrum Production'],
	['---------- Vision+ Payment ------------------------', '', '', '', ''],
	['vp-payment1', '10.10.20.91', '22', 'kris', 'Payment 1'],
	['vp-payment2', '10.10.20.92', '22', 'kris', 'Payment 1'], 
	['---------- Vision+ Indihome ------------------------', '', '', '', ''], 
	['vp-indihome-stag', '10.10.19.225', '22', 'kris', 'Indihome staging'],
 	['vp-indihome-lb1', '10.10.20.150', '45817', 'kris', 'Indihome LB 1'],
 	['vp-indihome-lb2', '10.10.20.151', '45817', 'kris', 'Indihome LB 2'],
 	['vp-indihome-lb3', '10.10.20.152', '45817', 'kris', 'Indihome LB 3'], 
	['vp-indihome-prod1', '10.10.21.8', '22', 'kris', 'Indihome Production'],
	['vp-indihome-prod2', '10.10.21.9', '22', 'kris', 'Indihome Production'],
	['vp-indihome-prod3', '10.10.21.10', '22', 'kris', 'Indihome Production'],
	['vp-indihome-prod4', '10.10.21.11', '22', 'kris', 'Indihome Production'],
	['vp-indihome-redis', '10.10.21.12', '22', 'kris', 'Indihome Production Redis'],
	['vp-indihome-db', '10.10.21.13', '22', 'kris', 'Indihome Production Postgres DB'],
	['---------- Vision+ Entitlement LB ------------------------', '', '', '', ''],
	['entitlement-lb-1', '10.10.20.123', '45817', 'kris', 'Entitlement LB 1'],
	['entitlement-lb-2', '10.10.20.124', '45817', 'kris', 'Entitlement LB 2'],
	['entitlement-lb-3', '10.10.20.125', '45817', 'kris', 'Entitlement LB 3'],
	['entitlement-lb-4', '10.10.20.126', '45817', 'kris', 'Entitlement LB 4'],
	['---------- Vision+ Entitlement ------------------------', '', '', '', ''],
	['entitlement-1', '10.10.20.95', '22', 'kris', 'Entitlement 1'],
	['entitlement-2', '10.10.20.96', '22', 'kris', 'Entitlement 2'],
	['entitlement-3', '10.10.21.95', '22', 'kris', 'Entitlement 3'],
	['entitlement-4', '10.10.21.96', '22', 'kris', 'Entitlement 4'],
	['entitlement-5', '10.10.21.97', '22', 'kris', 'Entitlement 5'],
	['---------- Vision+ Partners ------------------------', '', '', '', ''],
 	['partners-lb1', '10.10.20.150', '45817', 'kris', 'Partners LB 1'],
  	['partners-lb2', '10.10.20.151', '45817', 'kris', 'Partners LB 2'],
  	['partners-lb3', '10.10.20.152', '45817', 'kris', 'Partners LB 3'],
	['partners-node1', '10.10.19.151', '45817', 'kris', 'Partners Node 1'],
	['partners-node2', '10.10.19.152', '45817', 'kris', 'Partners Node 2'],
	['partners-node3', '10.10.19.153', '45817', 'kris', 'Partners Node 3'],
	['partners-node4', '10.10.19.154', '45817', 'kris', 'Partners Node 4'],
	['partners-node5', '10.10.19.155', '45817', 'kris', 'Partners Node 5'],
	['partners-node6', '10.10.19.156', '45817', 'kris', 'Partners Node 6'],
 	['---------- R+ /r hit ------------------------', '', '', '', ''], 
	['slash-r', '10.10.21.100', '22', 'kris', 'R+ /r hit'],
	['staging-python', '10.10.19.218', '22', 'kris', 'All Staging Python'],
 	['---------- Versioning ------------------------', '', '', '', ''],
 	['partners-lb1', '10.10.20.150', '45817', 'kris', 'Partners LB 1'],
 	['---------- V+ View Counts ------------------------', '', '', '', ''],
  	['views-count', '10.10.21.66', '22', 'kris', 'View Counts Node 1'],
  	['views-count2', '10.10.21.69', '22', 'kris', 'View Counts Node 2'],
 	['---------- V+ Analytics ------------------------', '', '', '', ''],
  	['analytics', '10.10.21.62', '22', 'kris', 'V+ Analytics'], 
 	['---------- V+ Partners Webview ------------------------', '', '', '', ''],
  	['partners-webview', '10.10.21.70', '22', 'kris', 'V+ Partners Webview API'],
 	['---------- V+ Sections ------------------------', '', '', '', ''],   
  	['sections', '10.10.21.23', '22', 'kris', 'V+ Sections'],
  	['sections-db', '10.10.21.21', '22', 'kris', 'V+ Sections DB'],
  	['sections-redis', '10.10.21.22', '22', 'kris', 'V+ Sections Redis'],
 	['---------- V+ Payment ------------------------', '', '', '', ''],   
  	['snap-notif-be', '10.10.21.92', '22', 'kris', 'V+ Snap Notification'],
 	['---------- V+ Miscellaneous ------------------------', '', '', '', ''],   
  	['telco-prov', '10.10.21.148', '22', 'kris', 'V+ Telco Provisioning'],
  	['badparenting', '10.10.20.50', '22', 'kris', 'V+ Bad Parenting Quiz'],   
 	['---------- V+ Cron DB ------------------------', '', '', '', ''],   
  	['cron-db', '10.10.21.52', '22', 'kris', 'V+ Cron DB'],   
  	['voucher-db', '10.10.21.174', '22', 'kris', 'V+ Voucher DB'],
 	['---------- V+ Markom CMS ------------------------', '', '', '', ''],   
  	['stag-markom-lb', '10.10.21.240', '22', 'kris', 'V+ LB Markom Staging'],   
  	['stag-markom-vm', '10.10.19.224', '22', 'kris', 'V+ VM Markom Staging'],
  	['prod-markom-lb', '10.10.20.127', '45817', 'kris', 'V+ LB Markom Prod'],   
  	['prod-markom-cms', '10.10.21.156', '22', 'kris', 'V+ VM Markom CMS'],
  	['prod-markom-cms2', '10.10.21.164', '22', 'kris', 'V+ VM Markom CMS 2'],
  	['prod-markom-db', '10.10.21.157', '22', 'kris', 'V+ VM Markom CMS DB'],   

  	['prod-purchase', '10.10.21.254', '22', 'kris', 'V+ VM Purchase V+ TV'],
   
  	['versioning', '10.10.20.57', '22', 'kris', 'V+ VM Purchase V+ TV'],
  	['versioning2', '10.10.20.58', '22', 'kris', 'V+ VM Purchase V+ TV'],    

  	['lb-payment', '10.10.20.121', '45817', 'kris', 'V+ LB Payment'],    
  	['payment1', '10.10.20.91', '22', 'kris', 'Payment'],    
  	['payment2', '10.10.20.92', '22', 'kris', 'Payment'],    
  	['payment3', '10.10.21.91', '22', 'kris', 'Payment'],
  	['paymentredis', '10.10.20.94', '22', 'kris', 'Payment Redis'],
   
  	['appconfig-stag', '10.10.21.241', '22', 'kris', 'AppConfig Stag'],   
]

private_keys = ['/Users/ksetyadi/.ssh/id_rsa', '/Users/ksetyadi/.ssh/id_rsa_mbp_2011']
