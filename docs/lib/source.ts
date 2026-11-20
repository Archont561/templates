import {loader, type Source} from 'fumadocs-core/source';
import {docs} from '@/.source';
import {createElement} from 'react';
import {BookOpen, Terminal, ShieldCheck, Wrench} from 'lucide-react';
const icons = {BookOpen, Terminal, ShieldCheck, Wrench};
export const source = loader({baseUrl:'/guide',source:({files:[...docs.docs.map(data=>({type:'page' as const,path:data._file.path,data})),...docs.meta.map(data=>({type:'meta' as const,path:data._file.path,data}))]} as Source<{pageData:(typeof docs.docs)[number];metaData:(typeof docs.meta)[number]}>),icon:(name)=>name && name in icons ? createElement(icons[name as keyof typeof icons]) : undefined});
