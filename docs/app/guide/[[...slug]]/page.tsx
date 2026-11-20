import {notFound} from 'next/navigation';
import {DocsPage,DocsBody,DocsTitle,DocsDescription} from 'fumadocs-ui/page';
import mdx from 'fumadocs-ui/mdx';
import {source} from '@/lib/source';
import {Tabs,Tab} from 'fumadocs-ui/components/tabs';
import {Files,File,Folder} from 'fumadocs-ui/components/files';
import {Steps,Step} from 'fumadocs-ui/components/steps';
import {Accordion,Accordions} from 'fumadocs-ui/components/accordion';
import {TypeTable} from 'fumadocs-ui/components/type-table';
import {Terminal, ShieldCheck, Wrench} from 'lucide-react';
type Props={params:Promise<{slug?:string[]}>};
export function generateStaticParams(){return source.generateParams()}
export async function generateMetadata({params}:Props){const p=source.getPage((await params).slug);return {title:p?.data.title,description:p?.data.description}}
export default async function Page({params}:Props){const page=source.getPage((await params).slug);if(!page)notFound();const Body=page.data.body;return <DocsPage toc={page.data.toc}><DocsTitle>{page.data.title}</DocsTitle><DocsDescription>{page.data.description}</DocsDescription><DocsBody><Body components={{...mdx,Tabs,Tab,Files,File,Folder,Steps,Step,Accordions,Accordion,TypeTable,Terminal,ShieldCheck,Wrench}}/></DocsBody></DocsPage>}
